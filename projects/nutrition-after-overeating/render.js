const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{
 const reel=process.argv[2]; const only=process.argv[3]; // optional single time (seconds) for stills
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.resolve('composition.html')+'?reel='+reel); await p.waitForFunction('window.READY');
 const total=await p.evaluate('TOTAL'); const hook=await p.evaluate('HOOK');
 if(only){await p.evaluate(t=>seek(t),+only);await p.screenshot({path:`renders/still_r${reel}_${only}.png`,omitBackground:true});await b.close();return}
 const dir=`/tmp/claude-0/frames${reel}`; fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir,{recursive:true});
 const n=Math.round(total*30);
 for(let i=0;i<n;i++){await p.evaluate(t=>seek(t),i/30);await p.screenshot({path:`${dir}/${String(i).padStart(4,'0')}.png`,omitBackground:true})}
 fs.writeFileSync(`${dir}/meta.json`,JSON.stringify({total,hook,n}));console.log('done',reel,n,total,hook);await b.close();
})();
