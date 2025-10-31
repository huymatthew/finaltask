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
function startCountdownTimer() {
  const targetDate = new Date('2025-11-09T00:00:00+07:00'); // 9/11/2025 00:00 Vietnam time
  const daysEl = document.getElementById('days');
  const hoursEl = document.getElementById('hours');
  const minutesEl = document.getElementById('minutes');
  const secondsEl = document.getElementById('seconds');

  if (!daysEl || !hoursEl || !minutesEl || !secondsEl) return;

  function updateCountdown() {
    const now = new Date();
    const difference = targetDate - now;

    if (difference > 0) {
      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      daysEl.textContent = days.toString().padStart(2, '0');
      hoursEl.textContent = hours.toString().padStart(2, '0');
      minutesEl.textContent = minutes.toString().padStart(2, '0');
      secondsEl.textContent = seconds.toString().padStart(2, '0');
    } else {
      daysEl.textContent = '00';
      hoursEl.textContent = '00';
      minutesEl.textContent = '00';
      secondsEl.textContent = '00';
    }
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);
};
startCountdownTimer();

function jumpscare() {
  
  const scriptEl = document.currentScript || document.querySelector('script[src$="script.js"]') || document.scripts[document.scripts.length-1];
  const baseUrl = scriptEl && scriptEl.src
    ? scriptEl.src.replace(/\/[^\/]*$/, '/')
    : (window.location.origin + '/static/');
  const audio = new Audio(new URL('sound/jumpscare.mp3', baseUrl).href);
  audio.play();
  const img = document.getElementById('jumpscare-img');
  if (img) {
    img.style.display = 'block';
    setTimeout(() => {
      img.style.display = 'none';
    }, 3000);
  }
}
