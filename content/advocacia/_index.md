---
title: 'Advocacia / Consultoria'
date: 2026-06-15
type: landing

sections:
  - block: markdown
    content:
      title: ''
      text: |-
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
        .adv{font-family:'Montserrat',system-ui,sans-serif;position:relative;left:50%;transform:translateX(-50%);width:min(1040px,92vw)}
        /* HERO — prévia do site do escritório com o título por cima (estrutura ref. DSR/Didier) */
        .adv-hero{text-align:center;padding:.5rem 0 3rem;border-bottom:1px solid rgba(157,180,204,.14)}
        .adv-hero h1{margin:0;color:#f3f4f6;font-weight:700;text-transform:uppercase;letter-spacing:.14em;font-size:clamp(1.5rem,4.2vw,2.55rem);line-height:1.18}
        .adv-hero h1 b{color:#d0835d;font-weight:700}
        .adv-hero__sub{margin:1rem 0 1.8rem;color:#9db4cc;font-size:.92rem;letter-spacing:.06em;text-transform:uppercase}
        .adv-frame{display:block;text-decoration:none;max-width:880px;margin:0 auto;border-radius:10px;overflow:hidden;border:1px solid rgba(157,180,204,.22);box-shadow:0 30px 70px -34px rgba(0,0,0,.95);transition:transform .25s ease,box-shadow .25s ease}
        .adv-frame:hover{transform:translateY(-4px);box-shadow:0 42px 86px -32px rgba(0,0,0,1)}
        .adv-frame__bar{display:flex;align-items:center;gap:.45rem;background:#15161a;padding:.6rem .85rem;border-bottom:1px solid rgba(157,180,204,.14)}
        .adv-frame__bar i{width:10px;height:10px;border-radius:50%;background:#3a3c44;display:inline-block}
        .adv-frame__url{margin-left:.6rem;color:#8a93a3;font-size:.74rem;letter-spacing:.04em}
        .adv-frame img{display:block;width:100%;height:auto}
        .adv-frame__hint{display:block;margin:1.1rem 0 0;color:#d0835d;font-size:.78rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase}
        /* Blocos de seção */
        .adv-block{padding:3.6rem 0;border-bottom:1px solid rgba(157,180,204,.1)}
        .adv-block:last-child{border-bottom:0}
        .adv-eye{display:block;text-align:center;color:#d0835d;font-weight:600;font-size:.76rem;letter-spacing:.24em;text-transform:uppercase;margin:0 0 .8rem}
        .adv-sec{text-align:center;color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.1em;font-size:clamp(1.15rem,2.6vw,1.5rem);margin:0 0 1.7rem}
        .adv-sec::after{content:'';display:block;width:54px;height:3px;background:#d0835d;margin:.95rem auto 0;border-radius:2px}
        .adv-lead{text-align:center;color:#e8ebef;font-weight:300;font-size:clamp(1.25rem,2.8vw,1.7rem);line-height:1.4;margin:0 auto 1.9rem;max-width:26ch}
        .adv-text{color:#cdd2da;line-height:1.95;font-size:1.04rem;max-width:66ch;margin:0 auto 1.15rem;text-align:center}
        .adv-text strong{color:#f3f4f6;font-weight:600}
        /* Botão sólido (CTA) */
        .adv-cta-wrap{text-align:center;margin:2.4rem 0 0}
        .adv-btn{display:inline-block;font-family:'Montserrat',sans-serif;font-weight:600;font-size:.8rem;letter-spacing:.13em;text-transform:uppercase;color:#0a0a0b;background:#d0835d;border:2px solid #d0835d;border-radius:0;padding:.85rem 2.1rem;text-decoration:none;transition:background .2s ease,color .2s ease}
        .adv-btn:hover{background:transparent;color:#d0835d}
        /* Área de atuação — segmentos em grade */
        .adv-areas{list-style:none;max-width:860px;margin:2rem auto 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:0}
        .adv-areas li{color:#cdd2da;font-size:.8rem;font-weight:500;text-transform:uppercase;letter-spacing:.07em;text-align:center;padding:1.05rem .5rem;border:1px solid rgba(157,180,204,.12);margin:-1px 0 0 -1px;transition:background .18s ease,color .18s ease}
        .adv-areas li:hover{color:#fff;background:rgba(208,131,93,.09)}
        @media(max-width:760px){.adv-areas{grid-template-columns:repeat(2,1fr)}}
        /* FAIXA BRANCA (logo + endereço + contatos), acima de Contato — ref. DSR */
        .adv-strip{background:#fff;border-top:4px solid #d0835d;border-radius:2px;margin:3.4rem 0 0;padding:2.4rem 2.2rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:2rem 3rem;box-shadow:0 26px 64px -32px rgba(0,0,0,.9)}
        .adv-strip__logo{width:min(240px,64vw);height:auto;flex:0 0 auto}
        .adv-strip__info{font-style:normal;color:#495057;line-height:1.75;font-size:.96rem;text-align:left;min-width:240px}
        .adv-strip__info strong{color:#1f2937;font-weight:700;display:block;margin:0 0 .35rem;font-size:1.02rem}
        .adv-strip__info a{color:#495057;text-decoration:none}
        .adv-strip__info a:hover{color:#d0835d}
        .adv-strip__info .sep{color:#cfcbc4;margin:0 .15rem}
        /* CONTATO — formulário (estrutura ref. DSR), tema escuro do site */
        .adv-form{max-width:620px;margin:0 auto;display:flex;flex-direction:column;gap:.35rem}
        .adv-form label{color:#9db4cc;font-size:.78rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin:.7rem 0 .3rem}
        .adv-form input,.adv-form textarea{font-family:'Montserrat',sans-serif;background:rgba(157,180,204,.06);border:1px solid rgba(157,180,204,.28);border-radius:4px;color:#eef1f5;font-size:1rem;padding:.7rem .85rem;transition:border-color .18s ease,background .18s ease}
        .adv-form input:focus,.adv-form textarea:focus{outline:none;border-color:#d0835d;background:rgba(208,131,93,.07)}
        .adv-form textarea{min-height:130px;resize:vertical}
        .adv-form button{align-self:center;margin-top:1.4rem;font-family:'Montserrat',sans-serif;font-weight:600;font-size:.82rem;letter-spacing:.13em;text-transform:uppercase;color:#0a0a0b;background:#d0835d;border:2px solid #d0835d;border-radius:0;padding:.8rem 2.4rem;cursor:pointer;transition:background .2s ease,color .2s ease}
        .adv-form button:hover{background:transparent;color:#d0835d}
        .adv-honey{display:none}
        </style>
        <div class="adv">

          <header class="adv-hero">
            <h1>Advocacia <b>&amp;</b> Consultoria</h1>
            <p class="adv-hero__sub">Cosmo &amp; Cosentino Advogados</p>
            <a class="adv-frame" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">
              <span class="adv-frame__bar"><i></i><i></i><i></i><span class="adv-frame__url">cosmocosentino.com</span></span>
              <img src="/img/cosmocosentino-preview.jpg" alt="Prévia do site Cosmo & Cosentino Advogados" loading="lazy">
            </a>
            <span class="adv-frame__hint">Visite o site do escritório →</span>
          </header>

          <section class="adv-block">
            <span class="adv-eye">Quem somos</span>
            <h2 class="adv-sec">Conheça o escritório</h2>
            <p class="adv-lead">Desde 2007, advocacia dedicada a pessoas e empresas.</p>
            <p class="adv-text">A sociedade teve início em <strong>2007</strong>, quando <strong>Sergio Cosmo</strong> e <strong>Carlo Cosentino</strong>, advogados desde 2000 e 2005, resolveram unir suas forças, constituindo, assim, o escritório <strong>Cosmo e Cosentino Advogados</strong>.</p>
            <p class="adv-text">O escritório nasceu do ideal comum dos seus sócios fundadores em empreender uma advocacia voltada à defesa de interesses de pessoas físicas com a mesma atenção e profissionalismo comumente dedicados aos seus clientes empresariais.</p>
            <p class="adv-text">O assessoramento às pessoas jurídicas ocorre tanto no contencioso judicial como na esfera consultiva, abrangendo empresas, organizações não governamentais e entidades de classe.</p>
            <div class="adv-cta-wrap">
              <a class="adv-btn" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">Acessar o site do escritório</a>
            </div>
          </section>

          <section class="adv-block">
            <span class="adv-eye">Atuação</span>
            <h2 class="adv-sec">Área de atuação</h2>
            <p class="adv-text">Histórico de atuação na defesa dos interesses de pessoas físicas, empresas, organizações não governamentais e entidades de classe. Intensa experiência em demandas relacionadas ao terceiro setor e às relações individuais e coletivas de trabalho.</p>
            <ul class="adv-areas">
              <li>Pessoas Físicas</li>
              <li>Empresas</li>
              <li>Organizações Não Governamentais</li>
              <li>Entidades de Classe</li>
              <li>Terceiro Setor</li>
              <li>Relações Individuais e Coletivas de Trabalho</li>
            </ul>
          </section>

          <div class="adv-strip">
            <img class="adv-strip__logo" src="/img/cosmo-consentino-brand.png" alt="Cosmo & Cosentino Advogados">
            <address class="adv-strip__info">
              <strong>Cosmo &amp; Cosentino Advogados</strong>
              Rua Frei Matias Teves, 280 — 305<br>
              Ilha do Leite, Recife / PE<br>
              <a href="https://wa.me/5581996372619" target="_blank" rel="noopener">WhatsApp (81) 99637-2619</a><span class="sep">·</span><a href="tel:+558130330089">Fone (81) 3033-0089</a><br>
              <a href="mailto:contato@cosmocosentino.com">contato@cosmocosentino.com</a>
            </address>
          </div>

          <section class="adv-block">
            <span class="adv-eye">Fale com o escritório</span>
            <h2 class="adv-sec">Contato</h2>
            <form class="adv-form" action="https://formsubmit.co/contato@cosmocosentino.com" method="POST">
              <input type="hidden" name="_subject" value="Contato pelo site — Advocacia (carlocosentino.com.br)">
              <input type="hidden" name="_captcha" value="false">
              <input type="hidden" name="_template" value="table">
              <input type="hidden" name="_next" value="https://www.carlocosentino.com.br/advocacia/?enviado=1">
              <input type="text" name="_honey" class="adv-honey">
              <label for="adv-nome">Seu nome</label>
              <input id="adv-nome" name="Nome" type="text" required>
              <label for="adv-email">Seu e-mail</label>
              <input id="adv-email" name="E-mail" type="email" required>
              <label for="adv-assunto">Assunto</label>
              <input id="adv-assunto" name="Assunto" type="text">
              <label for="adv-msg">Sua mensagem</label>
              <textarea id="adv-msg" name="Mensagem"></textarea>
              <button type="submit">Enviar</button>
            </form>
          </section>

        </div>
    design:
      columns: '1'
---
