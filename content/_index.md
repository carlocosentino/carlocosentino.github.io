---
title: ''
summary: ''
date: 2026-05-25
aliases:
  - /categories/
  - /feed/
type: landing

sections:
  - block: markdown
    content:
      text: |
        <style>
        .hero{position:relative;left:50%;transform:translateX(-50%);width:min(1140px,92vw);display:grid;grid-template-columns:minmax(330px,470px) minmax(0,1fr);gap:3rem;align-items:center;min-height:72vh;padding-top:4rem}
        .hero__photo{position:relative;display:flex;align-items:center;justify-content:center}
        .hero__photo picture{display:contents}
        .hero__photo img{width:100%;max-height:86vh;object-fit:contain;display:block;-webkit-mask-image:linear-gradient(to bottom,#000 85%,transparent 100%);mask-image:linear-gradient(to bottom,#000 85%,transparent 100%)}
        .hero__info{color:#e8e8ea;position:relative;z-index:2}
        .hero__kicker{letter-spacing:.2em;font-size:.72rem;text-transform:uppercase;color:#8aa0b4;font-weight:600}
        .hero__name{font-size:clamp(1.7rem,3vw,2.5rem);font-weight:700;line-height:1.05;margin:.2rem 0 .35rem;letter-spacing:-.01em}
        .hero__role{font-size:.92rem;color:#aebccb;font-weight:600;margin-bottom:.85rem}
        .hero__bio{font-size:.95rem;line-height:1.6;color:#c9ced6;max-width:42ch;text-align:justify}
        .hero__btn{display:inline-block;margin-top:1.1rem;padding:.58rem 1.15rem;border:1px solid #2c3340;border-radius:10px;color:#e8e8ea;text-decoration:none;font-weight:600;font-size:.9rem;transition:background .2s}
        .hero__btn:hover{background:#161a22}
        .hero__social{display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap}
        .hero__social a{color:#8aa0b4;text-decoration:none;font-size:.84rem;font-weight:500}
        .hero__social a:hover{color:#e8e8ea}
        @media(max-width:900px){.hero{grid-template-columns:1fr;text-align:center;min-height:auto;gap:1rem;padding-top:.5rem}.hero__photo{max-width:400px;margin:0 auto;background:none}.hero__photo img{height:auto;max-height:68vh;-webkit-mask-image:linear-gradient(to bottom,#000 86%,transparent 100%);mask-image:linear-gradient(to bottom,#000 86%,transparent 100%)}.hero__name{font-size:clamp(2rem,8vw,2.6rem)}.hero__bio{margin:0 auto;font-size:1rem}.hero__social{justify-content:center}}
        /* Home: espaçamento mais compacto entre as seções e entre título e conteúdo */
        .page-body section.hbb-section+section.hbb-section{padding-top:2.3rem!important;padding-bottom:2.3rem!important}
        .page-body section.hbb-section .flex.flex-col.gap-3{gap:.3rem!important}
        /* Mantém o hero colado no topo (a regra global de título não se aplica aqui) */
        #section-markdown{padding-top:0!important}
        </style>
        <div class="hero">
          <div class="hero__photo"><img src="/img/carlo-home-front-smile.webp" alt="Carlo Cosentino"></div>
          <div class="hero__info">
            <h1 class="hero__name">Carlo Cosentino</h1>
            <p class="hero__bio">Carlo Cosentino é advogado, sócio do escritório Cosmo e Cosentino Advogados, e Professor Adjunto da Faculdade de Direito do Recife – UFPE. Doutor e Mestre em Direito pela UFPE, investiga as relações entre o trabalho e a tecnologia – em especial as da informação e comunicação –, em diálogo com a teoria social crítica.</p>
            <a class="hero__btn" href="/perfil/">Saiba mais →</a>
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
      title: 'Podcast'
      text: |-
        Conversas sobre Direito do Trabalho, sindicalismo e os desafios do trabalho na era digital.

        <div class="pod-grid" data-pod-rss="https://anchor.fm/s/107f2f988/podcast/rss" data-pod-count="4" data-pod-cover="1">
          <a class="pod-card pod-card--cover" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Prescrio-e-Decadncia-Aula-de-Eduardo-Fortaleza---TGDT---09122025-e3c5k0h" target="_blank" rel="noopener"><img class="pod-card__cover" loading="lazy" src="https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_nologo/44183314/44183314-1754270063597-037daef5c1297.jpg" alt=""><span class="pod-card__body"><span class="pod-card__title">Prescrição e Decadência (Aula de Eduardo Fortaleza - TGDT - 09/12/2025)</span><span class="pod-card__meta">10 de dez. de 2025 · 56:38</span></span></a>
          <a class="pod-card pod-card--cover" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Contrato-de-emprego-e3c10hs" target="_blank" rel="noopener"><img class="pod-card__cover" loading="lazy" src="https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_nologo/44183314/44183314-1754270063597-037daef5c1297.jpg" alt=""><span class="pod-card__body"><span class="pod-card__title">Contrato de emprego</span><span class="pod-card__meta">07 de dez. de 2025 · 1:14:46</span></span></a>
          <a class="pod-card pod-card--cover" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Resoluo-do-Contrato-de-Emprego-07-08-2025-e36kpcb" target="_blank" rel="noopener"><img class="pod-card__cover" loading="lazy" src="https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_nologo/44183314/44183314-1754270063597-037daef5c1297.jpg" alt=""><span class="pod-card__body"><span class="pod-card__title">Resolução do Contrato de Emprego (07.08.2025)</span><span class="pod-card__meta">09 de ago. de 2025 · 41:28</span></span></a>
          <a class="pod-card pod-card--cover" href="https://podcasters.spotify.com/pod/show/carlo-cosentino/episodes/Resoluo-do-contrato-de-emprego-06-08-25-e36koru" target="_blank" rel="noopener"><img class="pod-card__cover" loading="lazy" src="https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_nologo/44183314/44183314-1754270063597-037daef5c1297.jpg" alt=""><span class="pod-card__body"><span class="pod-card__title">Resolução do contrato de emprego (06.08.25)</span><span class="pod-card__meta">09 de ago. de 2025 · 1:05:48</span></span></a>
        </div>

        <p class="more-row"><a class="more-link" href="/podcast/">Ver todos os episódios →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Vídeos'
      text: |-
        Aulas, palestras e entrevistas no canal do YouTube.

        <div class="yt-grid yt-grid--single">
          <a class="yt-card" href="https://www.youtube.com/watch?v=CyM0klkzuFU" target="_blank" rel="noopener"><div class="yt-card__thumb"><img loading="lazy" src="https://i.ytimg.com/vi/CyM0klkzuFU/hqdefault.jpg" alt=""><span class="yt-card__play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></div><div class="yt-card__title">Pod Cast - Tudo Bem Calculado | Conversa com Dr. Carlo Cosentino</div></a>
        </div>

        <p style="text-align:center;margin-top:1.2rem"><a class="section-cta" href="https://www.youtube.com/@carlocosentino" target="_blank" rel="noopener">▶ Ir para o canal no YouTube</a></p>

        <p class="more-row"><a class="more-link" href="/videos/">Ver todos os vídeos →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Material Didático'
      text: |-
        Planos de curso, roteiros de leitura, slides de aula e textos de referência em Direito do Trabalho e Direito Sindical.

        <p class="more-row"><a class="more-link" href="/materiais/">Ver o material didático →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Grupo de Pesquisa'
      text: |-
        **Direito do Trabalho e Teoria Social Crítica** (UFPE) – grupo coordenado por Carlo Cosentino que dá continuidade à linha do Prof. Everaldo Gaspar Lopes de Andrade, examinando o Direito do Trabalho sob inspiração filosófica e da teoria social crítica – do trabalho subordinado às crises do sindicalismo, da revolução informacional às metamorfoses do trabalho – e difundindo o pensamento da Escola do Recife.

        <p class="more-row"><a class="more-link" href="/projects/">Conhecer o grupo de pesquisa →</a></p>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Consultoria Jurídica'
      text: |-
        Atuação advocatícia de Carlo Cosentino como sócio do **Cosmo e Cosentino Advogados** (Recife, desde 2007): consultoria e contencioso em Direito do Trabalho e Direito Sindical, para pessoas físicas, empresas, sindicatos e entidades do terceiro setor – incluindo negociação coletiva e cálculos judiciais trabalhistas.

        <p class="more-row"><a class="more-link" href="/advocacia/">Conhecer a atuação →</a></p>
    design:
      columns: '1'
---
