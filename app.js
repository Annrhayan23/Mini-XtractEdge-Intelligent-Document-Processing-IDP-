async function upload(){
 let f=document.getElementById('file').files[0];
 let fd=new FormData(); fd.append("file",f);
 let r=await fetch("http://localhost:8000/process",{method:"POST",body:fd});
 document.getElementById('out').textContent=JSON.stringify(await r.json(),null,2);
}