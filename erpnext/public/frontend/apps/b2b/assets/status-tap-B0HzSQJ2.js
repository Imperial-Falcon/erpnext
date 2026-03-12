var d=(o,r,n)=>new Promise((s,t)=>{var i=e=>{try{a(n.next(e))}catch(c){t(c)}},l=e=>{try{a(n.throw(e))}catch(c){t(c)}},a=e=>e.done?s(e.value):Promise.resolve(e.value).then(i,l);a((n=n.apply(o,r)).next())});import{e as m,f as p,h as w,j as h,s as f}from"./index-BTKvHQNp.js";import"./frappe-ui-k2jwhJLy.js";/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */const v=()=>{const o=window;o.addEventListener("statusTap",()=>{m(()=>{const r=o.innerWidth,n=o.innerHeight,s=document.elementFromPoint(r/2,n/2);if(!s)return;const t=p(s);t&&new Promise(i=>w(t,i)).then(()=>{h(()=>d(void 0,null,function*(){t.style.setProperty("--overflow","hidden"),yield f(t,300),t.style.removeProperty("--overflow")}))})})})};export{v as startStatusTap};
//# sourceMappingURL=status-tap-B0HzSQJ2.js.map
