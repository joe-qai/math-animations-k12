/* 数益坊 · 站点交互（原生 JS，无依赖） */
(function () {
  'use strict';

  /* ---------------- 入场动效 ---------------- */
  var reveals = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  if (reveals.length) {
    if ('IntersectionObserver' in window) {
      var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0, rootMargin: '0px 0px 160px 0px' });
      reveals.forEach(function (el) { revealObserver.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* ---------------- 目录高亮 ---------------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var linkById = {};
    tocLinks.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var section = document.getElementById(id);
      if (section) linkById[id] = link;
    });

    var tocObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        tocLinks.forEach(function (l) { l.classList.remove('is-active'); });
        var active = linkById[entry.target.id];
        if (active) active.classList.add('is-active');
      });
    }, { rootMargin: '-18% 0px -68% 0px', threshold: 0 });

    Object.keys(linkById).forEach(function (id) {
      tocObserver.observe(document.getElementById(id));
    });
  }

  /* ---------------- 视频章节 ---------------- */
  var video = document.querySelector('[data-lesson-video]');
  var chapters = Array.prototype.slice.call(document.querySelectorAll('.chapter[data-t]'));

  /* preload="none"：页面打开时不拉视频，用户有播放意图（悬停/触摸/聚焦）时再取元数据 */
  if (video && video.getAttribute('preload') === 'none') {
    var warmVideo = function () {
      if (video.preload !== 'none') return;
      video.preload = 'metadata';
      try {
        video.load();
      } catch (err) {}
    };
    var videoCard = video.closest('.video-card') || video;
    ['pointerenter', 'touchstart', 'focusin'].forEach(function (evt) {
      videoCard.addEventListener(evt, warmVideo, { once: true, passive: true });
    });
  }

  if (video && chapters.length) {
    var chapterTimes = chapters.map(function (el) { return parseFloat(el.dataset.t); });

    var setActive = function (index) {
      chapters.forEach(function (el, i) {
        el.classList.toggle('is-active', i === index);
      });
    };

    var syncChapter = function () {
      var now = video.currentTime + 0.25;
      var index = 0;
      for (var i = 0; i < chapterTimes.length; i += 1) {
        if (now >= chapterTimes[i]) index = i;
      }
      setActive(index);
    };

    chapters.forEach(function (el, i) {
      el.addEventListener('click', function () {
        var target = chapterTimes[i];
        try {
          video.currentTime = target;
        } catch (err) {
          video.addEventListener('loadedmetadata', function once() {
            video.currentTime = target;
            video.removeEventListener('loadedmetadata', once);
          });
        }
        var played = video.play();
        if (played && typeof played.catch === 'function') played.catch(function () {});
        setActive(i);
      });
    });

    video.addEventListener('timeupdate', syncChapter);
    video.addEventListener('seeking', syncChapter);
    video.addEventListener('loadedmetadata', syncChapter);
  }

  /* ---------------- 随堂练习 ---------------- */
  function initQuiz(root) {
    var cards = Array.prototype.slice.call(root.querySelectorAll('.q'));
    var total = cards.length;
    var answered = 0;
    var score = 0;

    var progressEl = root.querySelector('[data-progress]');
    var barEl = root.querySelector('[data-bar]');
    var scoreEl = root.querySelector('[data-score]');
    var resultEl = root.querySelector('[data-result]');
    var resultScoreEl = root.querySelector('[data-result-score]');
    var resultTextEl = root.querySelector('[data-result-text]');
    var resetBtn = root.querySelector('[data-reset]');

    function paintProgress() {
      if (progressEl) progressEl.textContent = '已完成 ' + answered + ' / ' + total;
      if (barEl) barEl.style.width = (answered / total * 100) + '%';
      if (scoreEl) scoreEl.textContent = '得分 ' + score;
    }

    function showResult() {
      if (!resultEl) return;
      resultEl.classList.add('show');
      if (resultScoreEl) resultScoreEl.textContent = score + ' / ' + total;
      if (resultTextEl) {
        var text;
        if (score === total) {
          text = '全对。这一节可以过了，去下一节吧。';
        } else if (score * 2 >= total) {
          text = '基础已经稳了。把错题下面的解释再读一遍，比重新看视频更快。';
        } else {
          text = '建议回到视频，把相关章节重看一次，再回来做一遍这几道题。';
        }
        resultTextEl.textContent = text;
      }
    }

    cards.forEach(function (card) {
      var answer = parseInt(card.dataset.answer, 10);
      var options = Array.prototype.slice.call(card.querySelectorAll('.option'));
      var feedback = card.querySelector('.feedback');

      options.forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (card.classList.contains('is-done')) return;
          var chosen = parseInt(btn.dataset.i, 10);
          var isRight = chosen === answer;

          card.classList.add('is-done');
          options.forEach(function (b) {
            b.disabled = true;
            b.classList.toggle('is-dim', b !== btn && options.indexOf(b) !== answer);
          });
          btn.classList.add(isRight ? 'is-correct' : 'is-wrong');
          options[answer].classList.add('is-correct');

          if (feedback) {
            var explain = feedback.getAttribute('data-explain') || '';
            feedback.className = 'feedback show ' + (isRight ? 'ok' : 'no');
            feedback.innerHTML = (isRight ? '<b>答对了。</b> ' : '<b>再看一步：</b> ') + explain;
          }

          answered += 1;
          if (isRight) score += 1;
          paintProgress();

          if (answered === total) showResult();
        });
      });
    });

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        answered = 0;
        score = 0;
        cards.forEach(function (card) {
          card.classList.remove('is-done');
          Array.prototype.slice.call(card.querySelectorAll('.option')).forEach(function (b) {
            b.disabled = false;
            b.classList.remove('is-correct', 'is-wrong', 'is-dim');
          });
          var feedback = card.querySelector('.feedback');
          if (feedback) {
            feedback.className = 'feedback';
            feedback.textContent = '';
          }
        });
        if (resultEl) resultEl.classList.remove('show');
        paintProgress();
        root.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    }

    paintProgress();
  }

  Array.prototype.slice.call(document.querySelectorAll('[data-quiz]')).forEach(initQuiz);

  /* 兜底：页面未滚动（如打印、截图工具）时也保证内容全部可见 */
  if (reveals.length) {
    window.setTimeout(function () {
      reveals.forEach(function (el) { el.classList.add('in'); });
    }, 1600);
  }

  /* ---------------- 课时关键字搜索（全局，不分学段） ---------------- */
  var groups = Array.prototype.slice.call(document.querySelectorAll('.catalog-group'));
  var searchInput = document.getElementById('lesson-search');
  var clearBtn = document.querySelector('[data-search-clear]');
  var statusEl = document.querySelector('[data-search-status]');
  var emptyEl = document.querySelector('[data-search-empty]');

  function normalize(value) {
    return (value || '').toLowerCase().replace(/\s+/g, ' ').trim();
  }

  function applyFilter() {
    var query = searchInput ? normalize(searchInput.value) : '';
    var tokens = query ? query.split(' ') : [];
    var total = 0;

    groups.forEach(function (group) {
      var rail = group.querySelector('.lesson-grid');
      var cards = rail ? Array.prototype.slice.call(rail.querySelectorAll('.lesson-card')) : [];
      var shown = 0;

      cards.forEach(function (card) {
        var haystack = card.getAttribute('data-search') || '';
        var hit = true;
        for (var i = 0; i < tokens.length; i += 1) {
          if (haystack.indexOf(tokens[i]) === -1) { hit = false; break; }
        }
        card.hidden = !hit;
        if (hit) shown += 1;
      });

      group.hidden = tokens.length > 0 && shown === 0;
      total += shown;
      if (rail) rail.scrollLeft = 0;
    });

    if (statusEl) {
      statusEl.textContent = query ? '找到 ' + total + ' 节课' : '';
    }
    if (emptyEl) emptyEl.hidden = total !== 0;
    if (clearBtn) clearBtn.hidden = !query;
  }

  if (groups.length) {
    if (searchInput) {
      try {
        var initialQuery = new URLSearchParams(window.location.search).get('q');
        if (initialQuery) searchInput.value = initialQuery;
      } catch (err) { /* 忽略不支持 URLSearchParams 的老浏览器 */ }

      searchInput.addEventListener('input', applyFilter);
      searchInput.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
          searchInput.value = '';
          applyFilter();
        }
      });
    }

    if (clearBtn && searchInput) {
      clearBtn.addEventListener('click', function () {
        searchInput.value = '';
        applyFilter();
        searchInput.focus();
      });
    }

    applyFilter();
  }
}());