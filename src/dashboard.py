"""Interactive dashboard: one self-contained HTML file per run.

Embeds the run's JSON and renders client-side with vanilla JS — no network,
no dependencies, works from a double-click. `render_fragment` returns
body-content-only HTML (also used for claude.ai artifact publishing);
`write_dashboard` wraps it into a full page in output/.
"""
from __future__ import annotations

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

_CSS = """
:root{
  --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink-2:#52514e;
  --muted:#898781; --grid:#e1e0d9; --axis:#c3c2b7; --ring:rgba(11,11,11,.10);
  --s1:#2a78d6; --s2:#1baf7a; --s5:#4a3aa7;
  --good:#0ca30c; --warn:#fab219; --serious:#ec835a; --crit:#d03b3b;
  --wash:rgba(42,120,214,.08);
}
@media (prefers-color-scheme: dark){:root{
  --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink-2:#c3c2b7;
  --muted:#898781; --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,.10);
  --s1:#3987e5; --s2:#199e70; --s5:#9085e9; --wash:rgba(57,135,229,.12);
}}
:root[data-theme="light"]{
  --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink-2:#52514e;
  --muted:#898781; --grid:#e1e0d9; --axis:#c3c2b7; --ring:rgba(11,11,11,.10);
  --s1:#2a78d6; --s2:#1baf7a; --s5:#4a3aa7; --wash:rgba(42,120,214,.08);
}
:root[data-theme="dark"]{
  --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink-2:#c3c2b7;
  --muted:#898781; --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,.10);
  --s1:#3987e5; --s2:#199e70; --s5:#9085e9; --wash:rgba(57,135,229,.12);
}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);
  font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:24px 20px 64px}
h1{font-size:22px;margin:0}
h2{font-size:15px;margin:28px 0 10px;color:var(--ink)}
.sub{color:var(--muted);font-size:12.5px}
.card{background:var(--surface);border:1px solid var(--ring);border-radius:10px;padding:16px}
.row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.pill{display:inline-block;padding:3px 10px;border-radius:999px;font-weight:600;font-size:12.5px}
.pill.on{background:rgba(12,163,12,.14);color:var(--good)}
.pill.range{background:var(--wash);color:var(--s1)}
.pill.trans{background:rgba(250,178,25,.16);color:#8a6100}
:root[data-theme="dark"] .pill.trans,:root:not([data-theme="light"]) .pill.trans{color:var(--warn)}
.pill.off{background:rgba(208,59,59,.14);color:var(--crit)}
.sigs{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:8px;margin-top:12px}
.sig{border:1px solid var(--ring);border-radius:8px;padding:8px 10px;font-size:12.5px}
.sig b{display:block;font-size:12px;color:var(--ink-2);font-weight:600}
.sig .v{font-size:14px;font-weight:600}
.sig .rule{color:var(--muted);font-size:11.5px}
.ok{color:var(--good)} .fail{color:var(--crit)} .na{color:var(--muted)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:14px 0}
.tile{background:var(--surface);border:1px solid var(--ring);border-radius:10px;padding:10px 14px}
.tile .n{font-size:24px;font-weight:650}
.tile .l{color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.04em}
.split{display:grid;grid-template-columns:minmax(300px,5fr) minmax(320px,7fr);gap:14px}
@media(max-width:900px){.split{grid-template-columns:1fr}}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th{color:var(--muted);font-weight:600;text-align:left;padding:6px 8px;border-bottom:1px solid var(--axis)}
td{padding:6px 8px;border-bottom:1px solid var(--grid);font-variant-numeric:tabular-nums}
tr.sel td{background:var(--wash)}
.tblwrap{overflow-x:auto}
.controls{position:sticky;top:0;z-index:5;background:var(--page);padding:10px 0;border-bottom:1px solid var(--grid);margin-top:24px}
.controls .inner{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.ctl{display:flex;gap:6px;align-items:center;font-size:12.5px;color:var(--ink-2)}
.ctl label{font-weight:600}
.chip{cursor:pointer;user-select:none;padding:3px 10px;border-radius:999px;border:1px solid var(--axis);font-size:12px;color:var(--ink-2)}
.chip.act{background:var(--wash);border-color:var(--s1);color:var(--s1);font-weight:600}
select,input[type=range]{accent-color:var(--s1)}
select{background:var(--surface);color:var(--ink);border:1px solid var(--axis);border-radius:6px;padding:3px 6px;font-size:12.5px}
.count{margin-left:auto;color:var(--muted);font-size:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;margin-top:14px}
.idea h3{margin:0;font-size:16px}
.idea .head{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.badge{font-size:11px;padding:2px 8px;border-radius:999px;border:1px solid var(--axis);color:var(--ink-2)}
.badge.bo{background:rgba(74,58,167,.10);color:var(--s5);border-color:transparent}
.badge.pb{background:rgba(27,175,122,.12);color:var(--s2);border-color:transparent}
.badge.ai{background:rgba(235,104,52,.12);color:#c24e1f;border-color:transparent;font-weight:600}
:root:not([data-theme="light"]) .badge.ai{color:#eb8a5e}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]) .badge.ai{color:#c24e1f}}
.ooda{display:grid;gap:8px;margin-top:8px}
.ooda .ph b{display:block;font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.ooda .ph ul{margin:2px 0 0;padding-left:16px;font-size:12.5px;color:var(--ink-2)}
.ooda .ph li{margin-bottom:3px}
.score{margin-left:auto;font-weight:700;font-size:15px}
.thesis{color:var(--ink-2);font-size:12.5px;margin:6px 0 8px}
.lvls{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin:8px 0;text-align:center}
.lvl .k{font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em}
.lvl .x{font-weight:650;font-size:13.5px;font-variant-numeric:tabular-nums}
.lvl.stop .x{color:var(--crit)} .lvl.tgt .x{color:var(--good)} .lvl.entry .x{color:var(--s1)}
details{margin-top:8px;border-top:1px solid var(--grid);padding-top:8px}
summary{cursor:pointer;font-size:12.5px;font-weight:600;color:var(--ink-2)}
.steps{margin:8px 0 0;padding-left:18px;font-size:12.5px;color:var(--ink-2)}
.steps li{margin-bottom:5px}
.risks{list-style:none;margin:8px 0 0;padding:0;font-size:12.5px}
.risks li{display:flex;gap:8px;margin-bottom:6px;color:var(--ink-2)}
.dot{flex:none;width:9px;height:9px;border-radius:50%;margin-top:4px}
.dot.high{background:var(--crit)} .dot.medium{background:var(--warn)} .dot.info{background:var(--muted)}
.rlab{font-weight:700;font-size:10.5px;text-transform:uppercase;margin-top:1.5px}
.rlab.high{color:var(--crit)} .rlab.medium{color:#8a6100} .rlab.info{color:var(--muted)}
:root:not([data-theme="light"]) .rlab.medium{color:var(--warn)}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]) .rlab.medium{color:#8a6100}}
.spark{width:100%;height:130px;display:block}
svg text{font:10.5px system-ui,-apple-system,"Segoe UI",sans-serif;fill:var(--muted)}
.tip{position:fixed;pointer-events:none;background:var(--surface);border:1px solid var(--ring);
  border-radius:6px;padding:5px 8px;font-size:11.5px;color:var(--ink);box-shadow:0 2px 10px rgba(0,0,0,.18);
  display:none;z-index:20;white-space:nowrap}
.empty{padding:30px;text-align:center;color:var(--muted)}
.foot{margin-top:36px;color:var(--muted);font-size:11.5px;border-top:1px solid var(--grid);padding-top:12px}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:11.5px;color:var(--ink-2);margin-top:6px}
.legend span{display:inline-flex;align-items:center;gap:5px}
.sw{width:14px;height:3px;border-radius:2px;display:inline-block}
"""

_JS = r"""
const $=s=>document.querySelector(s), esc=t=>String(t).replace(/[&<>"]/g,
  c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const F={sectors:new Set(DATA.ideas.map(i=>i.sector)), setup:"ALL", minScore:0, minRR:0, sort:"total_score", theme:"all"};
const tip=document.createElement("div"); tip.className="tip"; document.body.appendChild(tip);
function showTip(e,html){tip.innerHTML=html;tip.style.display="block";
  tip.style.left=Math.min(e.clientX+14,innerWidth-tip.offsetWidth-8)+"px";
  tip.style.top=(e.clientY+14)+"px";}
function hideTip(){tip.style.display="none";}

const REGIME_CLASS={RISK_ON_TRENDING:"on",RISK_ON_RANGING:"range",TRANSITION:"trans",RISK_OFF:"off"};
const REGIME_HUMAN={RISK_ON_TRENDING:"Risk-on · trending",RISK_ON_RANGING:"Risk-on · ranging",
  TRANSITION:"Transition · mixed",RISK_OFF:"Risk-off · no new longs"};

function renderRegime(){
  const r=DATA.regime;
  $("#regime-pill").className="pill "+(REGIME_CLASS[r.label]||"trans");
  $("#regime-pill").textContent=REGIME_HUMAN[r.label]||r.label;
  $("#regime-expl").textContent=r.explanation;
  $("#sigs").innerHTML=r.signals.map(s=>{
    const v=s.passed===null?["·","na"]:(s.passed?["PASS","ok"]:["FAIL","fail"]);
    return `<div class="sig"><b>${esc(s.name)}</b><span class="v">${esc(s.value)}</span>
      <span class="${v[1]}" style="float:right;font-weight:700">${v[0]}</span>
      <div class="rule">${esc(s.rule)}</div></div>`;}).join("");
}

function renderFunnel(){
  const f=DATA.funnel, steps=[["Universe",f.universe],["Screened",f.screened],
    ["Candidates",f.candidates],["With setup",f.qualified],["Final ideas",f.ideas]];
  $("#funnel").innerHTML=steps.map(([l,n])=>
    `<div class="tile"><div class="n">${n}</div><div class="l">${l}</div></div>`).join("");
}

function renderRRG(){
  const rows=DATA.sectors.rows, W=440, H=330, m={t:16,r:14,b:30,l:40};
  const xs=rows.map(r=>r.rs_ratio), ys=rows.map(r=>r.rs_momentum);
  rows.forEach(r=>(r.trail||[]).forEach(p=>{xs.push(p.r);ys.push(p.m);}));
  const xpad=Math.max(2,(Math.max(...xs)-Math.min(...xs))*.12);
  const ypad=Math.max(2,(Math.max(...ys)-Math.min(...ys))*.12);
  const x0=Math.min(...xs)-xpad,x1=Math.max(...xs)+xpad,y0=Math.min(...ys)-ypad,y1=Math.max(...ys)+ypad;
  const X=v=>m.l+(v-x0)/(x1-x0)*(W-m.l-m.r), Y=v=>H-m.b-(v-y0)/(y1-y0)*(H-m.t-m.b);
  let g=`<rect x="${m.l}" y="${m.t}" width="${W-m.l-m.r}" height="${H-m.t-m.b}" fill="none" stroke="var(--grid)"/>`;
  if(100>x0&&100<x1) g+=`<line x1="${X(100)}" y1="${m.t}" x2="${X(100)}" y2="${H-m.b}" stroke="var(--axis)"/>`;
  if(0>y0&&0<y1) g+=`<line x1="${m.l}" y1="${Y(0)}" x2="${W-m.r}" y2="${Y(0)}" stroke="var(--axis)"/>`;
  const quad=[["Leading",x1,y1,"end","hanging"],["Improving",x0,y1,"start","hanging"],
    ["Weakening",x1,y0,"end","auto"],["Lagging",x0,y0,"start","auto"]];
  g+=quad.map(([t,qx,qy,a,b])=>`<text x="${X(qx)+(a=="end"?-6:6)}" y="${Y(qy)+(b=="hanging"?6:-6)}"
     text-anchor="${a}" dominant-baseline="${b}" font-weight="600">${t}</text>`).join("");
  g+=`<text x="${(m.l+W-m.r)/2}" y="${H-6}" text-anchor="middle">RS-ratio (vs SPY, 100 = neutral)</text>`;
  g+=`<text x="12" y="${(m.t+H-m.b)/2}" transform="rotate(-90 12 ${(m.t+H-m.b)/2})" text-anchor="middle">RS-momentum %</text>`;
  // labels greedily dodged vertically so clustered sectors stay readable
  const placed=[];
  rows.forEach(r=>{
    const c=r.selected?"var(--s1)":"var(--muted)";
    if(r.selected&&r.trail&&r.trail.length>1)
      g+=`<polyline points="${r.trail.slice(-3).map(p=>X(p.r)+","+Y(p.m)).join(" ")}" fill="none" stroke="${c}" stroke-width="1" opacity=".45"/>`;
    g+=`<circle class="pt" data-etf="${r.etf}" cx="${X(r.rs_ratio)}" cy="${Y(r.rs_momentum)}"
        r="${r.selected?6:4}" fill="${r.selected?c:"var(--surface)"}" stroke="${c}" stroke-width="2"/>`;
    let lx=X(r.rs_ratio)+8, ly=Y(r.rs_momentum)+3.5;
    for(let guard=0;guard<12&&placed.some(p=>Math.abs(p[0]-lx)<34&&Math.abs(p[1]-ly)<11);guard++) ly+=11;
    placed.push([lx,ly]);
    g+=`<text x="${lx}" y="${ly}" ${r.selected?'font-weight="700" fill="var(--ink-2)"':''}>${r.etf==="AI_INFRA"?"AI-infra":r.etf}</text>`;
  });
  $("#rrg").innerHTML=g;
  $("#rrg").querySelectorAll(".pt").forEach(el=>{
    const r=rows.find(q=>q.etf===el.dataset.etf);
    el.addEventListener("mousemove",e=>showTip(e,`<b>${r.etf}</b> ${esc(r.name)}<br>
      RS-ratio ${r.rs_ratio} · RS-mom ${r.rs_momentum}%<br>
      21d rel ${r.rel_21d}% · 63d rel ${r.rel_63d}%<br>${r.quadrant}${r.selected?" · selected #"+r.rank:""}`));
    el.addEventListener("mouseleave",hideTip);
  });
}

function renderSectorTable(){
  $("#sectbl").innerHTML=`<tr><th>ETF</th><th>Sector</th><th>21d rel</th><th>63d rel</th>
    <th>RS-ratio</th><th>Quadrant</th><th>Breadth</th><th>Sel</th></tr>`+
    DATA.sectors.rows.map(r=>`<tr class="${r.selected?"sel":""}"><td><b>${r.etf}</b></td>
      <td>${esc(r.name)}</td><td>${r.rel_21d>0?"+":""}${r.rel_21d}%</td>
      <td>${r.rel_63d>0?"+":""}${r.rel_63d}%</td><td>${r.rs_ratio}</td><td>${r.quadrant}</td>
      <td>${r.breadth==null?"—":Math.round(r.breadth*100)+"%"}</td>
      <td>${r.selected?"#"+r.rank:""}</td></tr>`).join("");
}

function sparkline(i){
  const W=340,H=130,m={t:8,r:58,b:16,l:8},cl=i.spark.close;
  const lv=[i.poc,i.vah,i.val,i.avwap,i.entry,i.stop,i.target];
  const lo=Math.min(...cl,...lv)*0.995, hi=Math.max(...cl,...lv)*1.005;
  const X=k=>m.l+k/(cl.length-1)*(W-m.l-m.r), Y=v=>m.t+(hi-v)/(hi-lo)*(H-m.t-m.b);
  const line=cl.map((v,k)=>(k?"L":"M")+X(k).toFixed(1)+" "+Y(v).toFixed(1)).join("");
  let g=`<rect x="${m.l}" y="${Y(i.vah)}" width="${W-m.l-m.r-m.l}" height="${Math.max(0,Y(i.val)-Y(i.vah))}" fill="var(--wash)"/>`;
  g+=`<line x1="${m.l}" x2="${W-m.r}" y1="${Y(i.poc)}" y2="${Y(i.poc)}" stroke="var(--s5)" stroke-dasharray="4 3" stroke-width="1.2"/>`;
  g+=`<line x1="${m.l}" x2="${W-m.r}" y1="${Y(i.avwap)}" y2="${Y(i.avwap)}" stroke="var(--s2)" stroke-dasharray="1.5 2.5" stroke-width="1.4"/>`;
  g+=`<path d="${line}" fill="none" stroke="var(--s1)" stroke-width="2" stroke-linejoin="round"/>`;
  // right-gutter level labels, dodged so they never overlap
  const marks=[["E",i.entry,"var(--s1)"],["S",i.stop,"var(--crit)"],["T",i.target,"var(--good)"]]
    .map(([t,v,c])=>({t,v,c,y:Math.max(m.t+4,Math.min(H-m.b-2,Y(v)))}))
    .sort((a,b)=>a.y-b.y);
  for(let k=1;k<marks.length;k++)
    if(marks[k].y-marks[k-1].y<12) marks[k].y=marks[k-1].y+12;
  marks.forEach(mk=>{
    g+=`<line x1="${W-m.r}" x2="${W-m.r+6}" y1="${Math.max(m.t+4,Math.min(H-m.b-2,Y(mk.v)))}" y2="${mk.y}" stroke="${mk.c}" stroke-width="1.5"/>`;
    g+=`<text x="${W-m.r+9}" y="${mk.y+3.5}" fill="${mk.c}" font-weight="700">${mk.t} ${mk.v}</text>`;});
  g+=`<rect class="hover" x="${m.l}" y="${m.t}" width="${W-m.l-m.r}" height="${H-m.t-m.b}" fill="transparent"/>`;
  g+=`<line class="xh" y1="${m.t}" y2="${H-m.b}" stroke="var(--axis)" style="display:none"/>`;
  return {svg:g,W,H,m,X,Y};
}

function ideaCard(i,rank){
  const sp=sparkline(i);
  const badge=i.setup==="ACCEPTANCE_BREAKOUT"?"bo":"pb";
  return `<div class="card idea" data-t="${i.ticker}">
    <div class="head"><h3>${rank}. ${i.ticker}</h3><span class="sub">${esc(i.name)}</span>
      <span class="score" title="structure × sector weight × RS percentile">${i.total_score}</span></div>
    <div class="row" style="gap:6px;margin-top:4px">
      <span class="badge ${badge}">${i.setup_human}</span>
      <span class="badge">${esc(i.sector)} #${i.sector_rank}</span>
      <span class="badge">RS p${i.rs_percentile}</span>
      <span class="badge">flow: ${i.flow_state}</span>
      ${i.theme?`<span class="badge ai" title="Passed the earnings + orders gate">⚡ AI infra · earnings-backed</span>`:""}</div>
    <p class="thesis">${esc(i.thesis)}</p>
    <svg class="spark" viewBox="0 0 ${sp.W} ${sp.H}" preserveAspectRatio="none">${sp.svg}</svg>
    <div class="legend"><span><span class="sw" style="background:var(--s1)"></span>close (126d)</span>
      <span><span class="sw" style="background:var(--s5)"></span>POC</span>
      <span><span class="sw" style="background:var(--s2)"></span>AVWAP</span>
      <span><span class="sw" style="background:var(--wash);height:8px"></span>value area</span></div>
    <div class="lvls">
      <div class="lvl entry"><div class="k">Entry</div><div class="x">${i.entry}</div></div>
      <div class="lvl stop"><div class="k">Stop</div><div class="x">${i.stop}</div></div>
      <div class="lvl tgt"><div class="k">Target</div><div class="x">${i.target}</div></div>
      <div class="lvl"><div class="k">R : R</div><div class="x">${i.rr}</div></div>
      <div class="lvl"><div class="k">Free-flow</div><div class="x">${i.free_flow}</div></div></div>
    <details><summary>How it executes (${i.execution.length} steps)</summary>
      <ol class="steps">${i.execution.map(s=>`<li>${esc(s)}</li>`).join("")}</ol></details>
    ${i.ooda?`<details open><summary>OODA — earnings &amp; orders check</summary>
      <div class="ooda">${["observe","orient","decide","act"].map(ph=>
        `<div class="ph"><b>${ph}</b><ul>${i.ooda[ph].map(x=>`<li>${esc(x)}</li>`).join("")}</ul></div>`).join("")}
      </div></details>`:""}
    <details open><summary>Risk remarks (${i.risks.length})</summary>
      <ul class="risks">${i.risks.map(r=>`<li><span class="dot ${r.level}"></span>
        <span><span class="rlab ${r.level}">${r.level}</span> ${esc(r.text)}</span></li>`).join("")}</ul></details>
  </div>`;
}

function attachSparkHover(card,i){
  const svg=card.querySelector(".spark"),hov=svg.querySelector(".hover"),xh=svg.querySelector(".xh");
  const sp={W:340,m:{l:8,r:58}};
  hov.addEventListener("mousemove",e=>{
    const r=svg.getBoundingClientRect();
    const fx=(e.clientX-r.left)/r.width*sp.W;
    const k=Math.max(0,Math.min(i.spark.close.length-1,
      Math.round((fx-sp.m.l)/(sp.W-sp.m.l-sp.m.r)*(i.spark.close.length-1))));
    const px=sp.m.l+k/(i.spark.close.length-1)*(sp.W-sp.m.l-sp.m.r);
    xh.setAttribute("x1",px);xh.setAttribute("x2",px);xh.style.display="";
    showTip(e,`<b>${i.ticker}</b> ${i.spark.dates[k]}<br>close ${i.spark.close[k]}`);
  });
  hov.addEventListener("mouseleave",()=>{xh.style.display="none";hideTip();});
}

function visibleIdeas(){
  return DATA.ideas.filter(i=>F.sectors.has(i.sector)&&
    (F.setup==="ALL"||i.setup===F.setup)&&i.total_score>=F.minScore&&i.rr>=F.minRR&&
    (F.theme==="all"||(F.theme==="exclude"?!i.theme:!!i.theme)))
    .sort((a,b)=>b[F.sort]-a[F.sort]);
}

function renderIdeas(){
  const v=visibleIdeas();
  $("#count").textContent=`showing ${v.length} of ${DATA.ideas.length} ideas`;
  const grid=$("#ideas");
  grid.innerHTML=v.length?v.map((i,k)=>ideaCard(i,k+1)).join("")
    :`<div class="card empty">No ideas match the current filters${DATA.ideas.length?"":" — the engine produced none this run"}.</div>`;
  v.forEach(i=>attachSparkHover(grid.querySelector(`[data-t="${i.ticker}"]`),i));
}

function renderControls(){
  const secs=[...new Set(DATA.ideas.map(i=>i.sector))];
  $("#secchips").innerHTML=secs.map(s=>
    `<span class="chip act" data-s="${esc(s)}">${esc(s)}</span>`).join("");
  $("#secchips").querySelectorAll(".chip").forEach(ch=>ch.addEventListener("click",()=>{
    const s=ch.dataset.s;
    if(F.sectors.has(s)&&F.sectors.size>1){F.sectors.delete(s);ch.classList.remove("act");}
    else{F.sectors.add(s);ch.classList.add("act");}
    renderIdeas();}));
  $("#setup").addEventListener("change",e=>{F.setup=e.target.value;renderIdeas();});
  $("#minscore").addEventListener("input",e=>{F.minScore=+e.target.value;
    $("#minscore-v").textContent=e.target.value;renderIdeas();});
  $("#minrr").addEventListener("input",e=>{F.minRR=+e.target.value;
    $("#minrr-v").textContent=(+e.target.value).toFixed(1);renderIdeas();});
  $("#sort").addEventListener("change",e=>{F.sort=e.target.value;renderIdeas();});
  $("#theme").addEventListener("change",e=>{F.theme=e.target.value;renderIdeas();});
}

function renderAppendix(){
  $("#watch").innerHTML=`<tr><th>Ticker</th><th>Sector</th><th>Structure score</th><th>Why it is only a watch</th></tr>`+
    (DATA.watch.map(w=>`<tr><td><b>${w.ticker}</b> <span class="sub">${esc(w.name)}</span></td>
     <td>${esc(w.sector)}</td><td>${w.score}</td><td>${esc(w.note)}</td></tr>`).join("")||
     `<tr><td colspan="4" class="sub">none</td></tr>`);
  $("#near").innerHTML=`<tr><th>Ticker</th><th>Sector</th><th>Failed filter</th></tr>`+
    (DATA.near_misses.map(n=>`<tr><td><b>${n.ticker}</b> <span class="sub">${esc(n.name)}</span></td>
     <td>${esc(n.sector)}</td><td>${esc(n.failed_filter)}</td></tr>`).join("")||
     `<tr><td colspan="3" class="sub">none</td></tr>`);
}

$("#run-date").textContent=DATA.run_date;
renderRegime();renderFunnel();renderRRG();renderSectorTable();renderControls();renderIdeas();renderAppendix();
"""


def render_fragment(data: dict) -> str:
    payload = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    return f"""<style>{_CSS}</style>
<div class="wrap">
  <div class="row" style="justify-content:space-between">
    <div><h1>Ideas Engine</h1>
      <div class="sub">US equities · 1–3 month position ideas · run <span id="run-date"></span></div></div>
    <span id="regime-pill" class="pill"></span>
  </div>

  <h2>① Macro regime</h2>
  <div class="card"><div id="regime-expl" style="font-weight:600"></div><div class="sigs" id="sigs"></div></div>

  <h2>Funnel</h2>
  <div class="tiles" id="funnel"></div>

  <h2>② Sector rotation (vs SPY)</h2>
  <div class="split">
    <div class="card"><svg id="rrg" viewBox="0 0 440 330" style="width:100%;height:auto"></svg></div>
    <div class="card tblwrap"><table id="sectbl"></table></div>
  </div>

  <h2>③ Ranked ideas</h2>
  <div class="controls"><div class="inner">
    <div class="ctl"><label>Sectors</label><span id="secchips" class="row" style="gap:6px"></span></div>
    <div class="ctl"><label>Setup</label>
      <select id="setup"><option value="ALL">All setups</option>
        <option value="ACCEPTANCE_BREAKOUT">Acceptance breakout</option>
        <option value="PULLBACK_TO_VALUE">Pullback to value</option></select></div>
    <div class="ctl"><label>Min score</label>
      <input type="range" id="minscore" min="0" max="100" value="0" step="5"><span id="minscore-v">0</span></div>
    <div class="ctl"><label>Min R:R</label>
      <input type="range" id="minrr" min="0" max="6" value="0" step="0.5"><span id="minrr-v">0.0</span></div>
    <div class="ctl"><label>AI infra</label>
      <select id="theme" title="AI-infrastructure theme names (all passed the earnings + orders gate)">
        <option value="all">Include</option>
        <option value="exclude">Exclude</option>
        <option value="only">Only theme</option></select></div>
    <div class="ctl"><label>Sort</label>
      <select id="sort"><option value="total_score">Total score</option>
        <option value="rr">Reward / risk</option><option value="rs_percentile">Relative strength</option>
        <option value="score">Structure score</option></select></div>
    <span class="count" id="count"></span>
  </div></div>
  <div class="grid" id="ideas"></div>

  <h2>④ Appendix</h2>
  <details><summary>Watch — structure present but no valid trade yet</summary>
    <div class="card tblwrap" style="margin-top:8px"><table id="watch"></table></div></details>
  <details><summary>Near-misses — failed exactly one screen filter</summary>
    <div class="card tblwrap" style="margin-top:8px"><table id="near"></table></div></details>

  <div class="foot">Generated {data["generated_at"]} · thresholds in config.yaml ·
    volume-flow is a daily proxy (true CVD needs intraday data) ·
    research tool — not investment advice.</div>
</div>
<script>const DATA={payload};\n{_JS}</script>
"""


def write_dashboard(data: dict) -> Path:
    frag = render_fragment(data)
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Ideas Engine — {data["run_date"]}</title></head><body>'
            f"{frag}</body></html>")
    path = OUTPUT_DIR / f"dashboard_{data['run_date']}.html"
    path.write_text(page, encoding="utf-8")
    # stable copy so a bookmarked URL (e.g. via tailscale serve) always
    # shows the latest run
    (OUTPUT_DIR / "index.html").write_text(page, encoding="utf-8")
    # macOS: also publish outside ~/Documents — the sandboxed Tailscale app
    # and launchd agents cannot read TCC-protected folders
    publish = Path("/Users/Shared/ideas-engine")
    if publish.parent.exists():
        publish.mkdir(exist_ok=True)
        (publish / "index.html").write_text(page, encoding="utf-8")
        (publish / path.name).write_text(page, encoding="utf-8")
    return path
