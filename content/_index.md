---
title: ''
summary: ''
date: 2026-05-25
type: landing

sections:
  - block: markdown
    content:
      text: |
        <style>
        .hero{position:relative;left:50%;transform:translateX(-50%);width:min(1140px,92vw);display:grid;grid-template-columns:minmax(330px,470px) minmax(0,1fr);gap:2.5rem;align-items:center;min-height:72vh;padding-top:4rem}
        .hero__photo{position:relative;display:flex;align-items:center;justify-content:center}
        .hero__photo picture{display:contents}
        .hero__photo img{width:100%;max-height:86vh;object-fit:contain;display:block;-webkit-mask-image:linear-gradient(to bottom,#000 85%,transparent 100%);mask-image:linear-gradient(to bottom,#000 85%,transparent 100%)}
        .hero__info{color:#e8e8ea;position:relative;z-index:2}
        .hero__kicker{letter-spacing:.2em;font-size:.72rem;text-transform:uppercase;color:#8aa0b4;font-weight:600}
        .hero__name{font-size:clamp(1.7rem,3vw,2.5rem);font-weight:700;line-height:1.05;margin:.2rem 0 .35rem;letter-spacing:-.01em}
        .hero__role{font-size:.92rem;color:#aebccb;font-weight:600;margin-bottom:.85rem}
        .hero__bio{font-size:.95rem;line-height:1.6;color:#c9ced6;max-width:42ch}
        .hero__btn{display:inline-block;margin-top:1.1rem;padding:.58rem 1.15rem;border:1px solid #2c3340;border-radius:10px;color:#e8e8ea;text-decoration:none;font-weight:600;font-size:.9rem;transition:background .2s}
        .hero__btn:hover{background:#161a22}
        .hero__social{display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap}
        .hero__social a{color:#8aa0b4;text-decoration:none;font-size:.84rem;font-weight:500}
        .hero__social a:hover{color:#e8e8ea}
        @media(max-width:900px){.hero{grid-template-columns:1fr;text-align:center;min-height:auto;gap:1rem;padding-top:.5rem}.hero__photo{max-width:400px;margin:0 auto;background:none}.hero__photo img{height:auto;max-height:68vh;-webkit-mask-image:linear-gradient(to bottom,#000 86%,transparent 100%);mask-image:linear-gradient(to bottom,#000 86%,transparent 100%)}.hero__name{font-size:clamp(2rem,8vw,2.6rem)}.hero__bio{margin:0 auto;font-size:1rem}.hero__social{justify-content:center}}
        </style>
        <div class="hero">
          <div class="hero__photo"><img src="/img/carlo-cutout.png" alt="Carlo Cosentino"></div>
          <div class="hero__info">
            <h1 class="hero__name">Carlo Cosentino</h1>
            <div class="hero__role">Professor Adjunto · Faculdade de Direito do Recife · UFPE</div>
            <p class="hero__bio">Carlo Cosentino é advogado, sócio do escritório Cosmo e Cosentino Advogados, e Professor Adjunto da Faculdade de Direito do Recife – UFPE. Doutor e Mestre em Direito pela UFPE, investiga as relações entre o trabalho e a tecnologia – em especial as da informação e comunicação –, em diálogo com a teoria social crítica.</p>
            <a class="hero__btn" href="/perfil/">Saiba mais →</a>
            <div class="hero__social">
              <a href="mailto:contato@carlocosentino.com.br">Contato</a>
              <a href="https://orcid.org/0000-0002-7661-4688" target="_blank" rel="noopener">ORCID</a>
              <a href="https://scholar.google.com/citations?user=8O4wNSUAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
              <a href="http://lattes.cnpq.br/9403069473693221" target="_blank" rel="noopener">Lattes</a>
              <a href="https://ufpe.academia.edu/CarloCosentino" target="_blank" rel="noopener">Academia.edu</a>
              <a href="https://www.researchgate.net/profile/Carlo-Cosentino-3" target="_blank" rel="noopener">ResearchGate</a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
  - block: collection
    id: papers
    content:
      title: Publicações
      count: 10
      sort_by: Weight
      order: desc
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: markdown
    content:
      text: |
        <p class="more-row"><a class="more-link" href="/publication/">Ver todas as publicações →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Vídeos'
      text: |-
        Aulas, palestras e entrevistas no canal do YouTube.

        <div class="yt-grid" data-yt-channel="UCAFgy5Xv0HOnfrDhJpTyQmQ" data-yt-count="4">
          <a class="yt-card" href="https://www.youtube.com/watch?v=1-b0G15XjLc" target="_blank" rel="noopener"><div class="yt-card__thumb"><img loading="lazy" src="https://i.ytimg.com/vi/1-b0G15XjLc/hqdefault.jpg" alt=""><span class="yt-card__play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></div><div class="yt-card__title">O trabalho remoto. Revolução, escravização, ativismo digital — alertas e direitos</div></a>
          <a class="yt-card" href="https://www.youtube.com/watch?v=yya3iUfPr8c" target="_blank" rel="noopener"><div class="yt-card__thumb"><img loading="lazy" src="https://i.ytimg.com/vi/yya3iUfPr8c/hqdefault.jpg" alt=""><span class="yt-card__play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></div><div class="yt-card__title">Participação de Carlo Cosentino no programa Roda Viva PE</div></a>
          <a class="yt-card" href="https://www.youtube.com/watch?v=Uqvxmwj0mmo" target="_blank" rel="noopener"><div class="yt-card__thumb"><img loading="lazy" src="https://i.ytimg.com/vi/Uqvxmwj0mmo/hqdefault.jpg" alt=""><span class="yt-card__play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></div><div class="yt-card__title">Carlo Cosentino entrevista Ricardo Antunes</div></a>
          <a class="yt-card" href="https://www.youtube.com/watch?v=fiOtZ8ES8nU" target="_blank" rel="noopener"><div class="yt-card__thumb"><img loading="lazy" src="https://i.ytimg.com/vi/fiOtZ8ES8nU/hqdefault.jpg" alt=""><span class="yt-card__play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></div><div class="yt-card__title">Seminário multidisciplinar: metamorfoses e crises do trabalho e do sindicalismo contemporâneo</div></a>
        </div>

        <p class="more-row"><a class="more-link" href="/videos/">Ver todos os vídeos →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Podcast'
      text: |-
        Conversas sobre Direito do Trabalho, sindicalismo e os desafios do trabalho na era digital.

        <div class="pod-grid" data-pod-rss="https://anchor.fm/s/107f2f988/podcast/rss" data-pod-count="4">
          <a class="pod-card" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Prescrio-e-Decadncia-Aula-de-Eduardo-Fortaleza---TGDT---09122025-e3c5k0h" target="_blank" rel="noopener"><span class="pod-card__icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.5 17.3c-.22.36-.68.47-1.04.25-2.86-1.75-6.46-2.14-10.7-1.17-.41.09-.82-.16-.92-.57-.09-.41.16-.82.57-.92 4.64-1.06 8.62-.61 11.83 1.35.36.22.47.68.25 1.06zm1.47-3.27c-.28.45-.86.59-1.31.32-3.27-2.01-8.26-2.6-12.13-1.42-.5.15-1.04-.13-1.19-.63-.15-.51.13-1.04.63-1.19 4.42-1.34 9.92-.68 13.67 1.62.44.27.59.86.33 1.3zm.13-3.4C16.7 8.5 10.66 8.3 6.92 9.43c-.61.18-1.25-.16-1.43-.76-.18-.61.16-1.25.77-1.43 4.3-1.3 10.95-1.05 15.27 1.52.55.32.73 1.04.4 1.59-.32.55-1.04.73-1.59.4z"/></svg></span><span class="pod-card__body"><span class="pod-card__title">Prescrição e Decadência (Aula de Eduardo Fortaleza - TGDT - 09/12/2025)</span><span class="pod-card__date">10 de dez. de 2025</span></span></a>
          <a class="pod-card" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Contrato-de-emprego-e3c10hs" target="_blank" rel="noopener"><span class="pod-card__icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.5 17.3c-.22.36-.68.47-1.04.25-2.86-1.75-6.46-2.14-10.7-1.17-.41.09-.82-.16-.92-.57-.09-.41.16-.82.57-.92 4.64-1.06 8.62-.61 11.83 1.35.36.22.47.68.25 1.06zm1.47-3.27c-.28.45-.86.59-1.31.32-3.27-2.01-8.26-2.6-12.13-1.42-.5.15-1.04-.13-1.19-.63-.15-.51.13-1.04.63-1.19 4.42-1.34 9.92-.68 13.67 1.62.44.27.59.86.33 1.3zm.13-3.4C16.7 8.5 10.66 8.3 6.92 9.43c-.61.18-1.25-.16-1.43-.76-.18-.61.16-1.25.77-1.43 4.3-1.3 10.95-1.05 15.27 1.52.55.32.73 1.04.4 1.59-.32.55-1.04.73-1.59.4z"/></svg></span><span class="pod-card__body"><span class="pod-card__title">Contrato de emprego</span><span class="pod-card__date">07 de dez. de 2025</span></span></a>
          <a class="pod-card" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Resoluo-do-Contrato-de-Emprego-07-08-2025-e36kpcb" target="_blank" rel="noopener"><span class="pod-card__icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.5 17.3c-.22.36-.68.47-1.04.25-2.86-1.75-6.46-2.14-10.7-1.17-.41.09-.82-.16-.92-.57-.09-.41.16-.82.57-.92 4.64-1.06 8.62-.61 11.83 1.35.36.22.47.68.25 1.06zm1.47-3.27c-.28.45-.86.59-1.31.32-3.27-2.01-8.26-2.6-12.13-1.42-.5.15-1.04-.13-1.19-.63-.15-.51.13-1.04.63-1.19 4.42-1.34 9.92-.68 13.67 1.62.44.27.59.86.33 1.3zm.13-3.4C16.7 8.5 10.66 8.3 6.92 9.43c-.61.18-1.25-.16-1.43-.76-.18-.61.16-1.25.77-1.43 4.3-1.3 10.95-1.05 15.27 1.52.55.32.73 1.04.4 1.59-.32.55-1.04.73-1.59.4z"/></svg></span><span class="pod-card__body"><span class="pod-card__title">Resolução do Contrato de Emprego (07.08.2025)</span><span class="pod-card__date">09 de ago. de 2025</span></span></a>
          <a class="pod-card" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Resoluo-do-contrato-de-emprego-06-08-25-e36koru" target="_blank" rel="noopener"><span class="pod-card__icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.5 17.3c-.22.36-.68.47-1.04.25-2.86-1.75-6.46-2.14-10.7-1.17-.41.09-.82-.16-.92-.57-.09-.41.16-.82.57-.92 4.64-1.06 8.62-.61 11.83 1.35.36.22.47.68.25 1.06zm1.47-3.27c-.28.45-.86.59-1.31.32-3.27-2.01-8.26-2.6-12.13-1.42-.5.15-1.04-.13-1.19-.63-.15-.51.13-1.04.63-1.19 4.42-1.34 9.92-.68 13.67 1.62.44.27.59.86.33 1.3zm.13-3.4C16.7 8.5 10.66 8.3 6.92 9.43c-.61.18-1.25-.16-1.43-.76-.18-.61.16-1.25.77-1.43 4.3-1.3 10.95-1.05 15.27 1.52.55.32.73 1.04.4 1.59-.32.55-1.04.73-1.59.4z"/></svg></span><span class="pod-card__body"><span class="pod-card__title">Resolução do contrato de emprego (06.08.25)</span><span class="pod-card__date">09 de ago. de 2025</span></span></a>
        </div>

        <p class="more-row"><a class="more-link" href="/podcast/">Ver todos os episódios →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Advocacia'
      text: |-
        **[Cosmo e Cosentino Advogados](https://www.cosmocosentino.com)** — atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor.
    design:
      columns: '1'
---
