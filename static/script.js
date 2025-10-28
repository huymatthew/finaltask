// script.js — đơn giản: nút đăng ký là placeholder
document.addEventListener('DOMContentLoaded', function(){
  // register button logic
  var btn = document.getElementById('register-btn');
  if(btn){
    btn.addEventListener('click', function(e){
      e.preventDefault();
      var link = btn.getAttribute('data-link') || btn.getAttribute('href');
      if(link && link !== '#' && link.trim() !== ''){
        window.location.href = link;
        return;
      }
      showNotice('Link đăng ký sẽ được gán sau. Bạn có thể cập nhật thuộc tính href hoặc data-link cho nút.');
    });
  }

  // mobile nav toggle (works for header nav and clones)
  function setupNavToggle(toggleId, navId){
    var t = document.getElementById(toggleId);
    var nav = document.getElementById(navId);
    if(!t || !nav) return;
    t.addEventListener('click', function(){
      var expanded = t.getAttribute('aria-expanded') === 'true';
      t.setAttribute('aria-expanded', String(!expanded));
      nav.classList.toggle('open');
    });
  }
  setupNavToggle('nav-toggle','main-nav');
  setupNavToggle('nav-toggle-2','main-nav-2');
  setupNavToggle('nav-toggle-3','main-nav-3');

  function showNotice(text){
    var n = document.createElement('div');
    n.className = 'notice';
    n.textContent = text;
    Object.assign(n.style,{position:'fixed',right:'18px',bottom:'18px',background:'#111',color:'#ffdede',padding:'10px 14px',border:'1px solid rgba(179,0,0,0.12)',borderRadius:'6px',zIndex:9999,boxShadow:'0 8px 30px rgba(0,0,0,0.6)'});
    document.body.appendChild(n);
    setTimeout(function(){ n.style.opacity='0'; n.style.transition='opacity .6s'; },3000);
    setTimeout(function(){ n.remove(); },3800);
  }
});
