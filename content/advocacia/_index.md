---
title: 'Advocacia / Consultoria'
date: 2026-06-15
type: landing

sections:
  - block: markdown
    content:
      title: 'Advocacia / Consultoria'
      text: |-
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
        .adv-wrap{position:relative;left:50%;transform:translateX(-50%);width:min(940px,92vw)}
        /* Lead editorial (inspirado na pág. de advocacia do escritório DSR) */
        .adv-lead{text-align:center;color:#e8ebef;font-weight:300;font-size:clamp(1.35rem,3.4vw,2rem);line-height:1.35;letter-spacing:.01em;margin:0 0 2.4rem}
        .adv-lead span{color:#9db4cc}
        .adv-intro{color:#cdd2da;line-height:1.9;font-size:1.06rem;text-align:justify;text-justify:inter-word;margin:0 0 1rem;max-width:62ch;margin-left:auto;margin-right:auto}
        .adv-intro strong{color:#f3f4f6;font-weight:600}
        /* Título de seção "áreas de atuação" */
        .adv-h{text-align:center;color:#f3f4f6;font-weight:600;font-size:1.55rem;letter-spacing:.005em;margin:3.4rem 0 .5rem}
        .adv-h+.adv-hsub{text-align:center;color:#8a93a3;font-size:.82rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;margin:0 0 2rem}
        /* Lista de áreas em colunas, estilo editorial (sem pílulas) */
        .adv-areas{list-style:none;margin:0 0 3rem;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:0 2.4rem;max-width:760px;margin-left:auto;margin-right:auto}
        .adv-areas li{color:#cdd2da;font-size:1rem;line-height:1.5;padding:.85rem .2rem;border-bottom:1px solid rgba(157,180,204,.16);transition:color .18s ease}
        .adv-areas li::before{content:'';display:inline-block;width:14px;height:2px;background:#d0835d;vertical-align:middle;margin-right:.7rem;opacity:.85}
        .adv-areas li:hover{color:#fff}
        @media(max-width:720px){.adv-areas{grid-template-columns:repeat(2,1fr);gap:0 1.4rem}}
        @media(max-width:440px){.adv-areas{grid-template-columns:1fr}}
        /* Banner com a identidade visual do escritório: claro, sóbrio, accent #d0835d, Open Sans */
        .adv-banner{display:block;text-align:center;text-decoration:none;font-family:'Open Sans',sans-serif;background:#ffffff;border:1px solid #e6e4e0;border-top:4px solid #d0835d;border-radius:2px;padding:3.2rem 2.4rem;box-shadow:0 26px 64px -30px rgba(0,0,0,.9);transition:transform .22s ease,box-shadow .22s ease}
        .adv-banner:hover{transform:translateY(-4px);box-shadow:0 36px 76px -28px rgba(0,0,0,.95)}
        .adv-banner__logo{width:min(300px,74%);height:auto;display:block;margin:0 auto 1.6rem}
        .adv-banner__desc{display:block;max-width:48ch;margin:0 auto 2rem;color:#495057;font-size:1rem;line-height:1.7}
        .adv-banner__cta{display:inline-block;font-weight:700;font-size:.84rem;letter-spacing:.09em;text-transform:uppercase;color:#d0835d;border:2px solid #d0835d;border-radius:0;padding:.72rem 1.9rem;transition:background .2s ease,color .2s ease}
        .adv-banner:hover .adv-banner__cta{background:#d0835d;color:#fff}
        /* Bloco de contato do escritório */
        .adv-contato{margin:3.4rem auto 0;max-width:640px;text-align:center}
        .adv-contato__h{color:#f3f4f6;font-weight:600;font-size:1.15rem;letter-spacing:.005em;margin:0 0 .9rem}
        .adv-contato__addr{color:#cdd2da;line-height:1.75;font-size:1rem;font-style:normal;margin:0 0 1.4rem}
        .adv-contato__links{list-style:none;display:flex;flex-wrap:wrap;justify-content:center;gap:.7rem 1rem;margin:0;padding:0}
        .adv-contato__links a{display:inline-flex;align-items:center;color:#9db4cc;text-decoration:none;font-size:.95rem;border:1px solid rgba(157,180,204,.3);border-radius:999px;padding:.5rem 1.15rem;transition:background .18s ease,color .18s ease,border-color .18s ease}
        .adv-contato__links a:hover{background:rgba(157,180,204,.1);color:#fff;border-color:rgba(157,180,204,.55)}
        </style>
        <div class="adv-wrap">
          <p class="adv-lead">Rigor acadêmico e prática profissional<br><span>a serviço do mundo do trabalho.</span></p>
          <p class="adv-intro">A atuação advocatícia de <strong>Carlo Cosentino</strong> nasce do encontro entre a pesquisa científica e o exercício cotidiano da profissão. Como sócio do escritório <strong>Cosmo &amp; Cosentino Advogados</strong>, conduz uma advocacia consultiva e contenciosa atenta às transformações do mundo do trabalho — do dissídio individual à negociação coletiva, da prevenção de litígios à atuação estratégica em juízo.</p>
          <p class="adv-intro">Cada caso é tratado com a mesma seriedade dedicada à investigação acadêmica: análise técnica rigorosa, leitura crítica da jurisprudência e soluções construídas sob medida para empresas, entidades do terceiro setor e trabalhadores.</p>

          <h2 class="adv-h">Áreas de atuação</h2>
          <p class="adv-hsub">consultoria e contencioso</p>
          <ul class="adv-areas">
            <li>Direito do Trabalho</li>
            <li>Direito Sindical</li>
            <li>Negociação Coletiva</li>
            <li>Terceiro Setor</li>
            <li>Consultoria Preventiva</li>
            <li>Contencioso Trabalhista</li>
          </ul>

          <a class="adv-banner" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">
            <img class="adv-banner__logo" src="/img/cosmo-consentino-brand.png" alt="Cosmo & Cosentino Advogados">
            <span class="adv-banner__desc">Atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor. Conheça o escritório no site institucional.</span>
            <span class="adv-banner__cta">Acessar o site do escritório</span>
          </a>

          <div class="adv-contato">
            <p class="adv-contato__h">Cosmo &amp; Cosentino Advogados</p>
            <address class="adv-contato__addr">Rua Frei Matias Teves, 280 — 305<br>Ilha do Leite, Recife / PE</address>
            <ul class="adv-contato__links">
              <li><a href="https://wa.me/5581996372619" target="_blank" rel="noopener">WhatsApp (81) 99637-2619</a></li>
              <li><a href="tel:+558130330089">Fone (81) 3033-0089</a></li>
              <li><a href="mailto:contato@cosmocosentino.com">contato@cosmocosentino.com</a></li>
            </ul>
          </div>
        </div>
    design:
      columns: '1'
---
