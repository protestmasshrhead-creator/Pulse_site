(function(){
  var sw=document.querySelector('.lang-sw'); if(!sw) return;
  var btn=sw.querySelector('.lang-btn'), menu=sw.querySelector('.lang-menu');
  function close(){menu.hidden=true;sw.classList.remove('open');btn.setAttribute('aria-expanded','false');}
  btn.addEventListener('click',function(e){e.stopPropagation();
    if(menu.hidden){menu.hidden=false;sw.classList.add('open');btn.setAttribute('aria-expanded','true');}else close();});
  document.addEventListener('click',function(e){if(!sw.contains(e.target))close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  menu.addEventListener('click',function(e){var a=e.target.closest('a[data-lang]');if(a){close();}});
})();
