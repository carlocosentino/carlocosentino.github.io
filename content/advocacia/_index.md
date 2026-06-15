---
title: 'Advocacia e Consultoria'
date: 2026-06-15
type: landing

sections:
  - block: markdown
    content:
      title: 'Advocacia e Consultoria'
      text: |-
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
        .adv{font-family:'Montserrat',system-ui,sans-serif;position:relative;left:50%;transform:translateX(-50%);width:min(1040px,92vw)}
        /* SEÇÃO "CONHEÇA O ESCRITÓRIO" com as fotos (rotativas) ao fundo */
        .adv-esc{position:relative;border-radius:12px;overflow:hidden;padding:3.2rem 2.6rem;border:1px solid rgba(157,180,204,.18);box-shadow:0 30px 70px -34px rgba(0,0,0,.95)}
        .adv-esc__slide{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;opacity:0;animation:advfade 18s infinite}
        .adv-esc__slide:nth-child(1){animation-delay:0s}
        .adv-esc__slide:nth-child(2){animation-delay:6s}
        .adv-esc__slide:nth-child(3){animation-delay:12s}
        @keyframes advfade{0%{opacity:0}2%{opacity:1}30%{opacity:1}34%{opacity:0}100%{opacity:0}}
        .adv-esc__ov{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(10,10,11,.82),rgba(10,10,11,.88))}
        .adv-esc__in{position:relative;z-index:2}
        .adv-esc__title{text-align:center;color:#fff;text-transform:uppercase;letter-spacing:.18em;font-weight:600;font-size:clamp(1.05rem,2.5vw,1.55rem);margin:0 0 2.2rem;text-shadow:0 2px 18px rgba(0,0,0,.6)}
        .adv-cols{display:grid;grid-template-columns:1.05fr .95fr;gap:2.8rem;align-items:center}
        .adv-sub{color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:clamp(1.1rem,2.4vw,1.4rem);margin:0 0 1.2rem;position:relative;padding-bottom:.7rem}
        .adv-sub::after{content:'';position:absolute;left:0;bottom:0;width:52px;height:3px;background:#d0835d;border-radius:2px}
        .adv-cols__text p{color:#e3e7ec;line-height:1.9;font-size:1.02rem;text-align:left;margin:0 0 1.05rem;text-shadow:0 1px 10px rgba(0,0,0,.45)}
        .adv-cols__text p:last-child{margin-bottom:0}
        .adv-cols__text strong{color:#fff;font-weight:600}
        .adv-officecard{text-align:center}
        .adv-officecard__logo{width:min(280px,82%);height:auto;display:block;margin:0 auto 1.4rem}
        .adv-officecard__desc{color:#dfe4ea;font-size:.97rem;line-height:1.65;margin:0 0 1.6rem;text-shadow:0 1px 10px rgba(0,0,0,.45)}
        .adv-officecard__btn{display:inline-block;font-weight:600;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:#fff;border:2px solid #d0835d;border-radius:0;padding:.72rem 1.7rem;text-decoration:none;transition:background .2s ease,color .2s ease}
        .adv-officecard__btn:hover{background:#d0835d;color:#0a0a0b}
        /* ÁREA DE ATUAÇÃO */
        .adv-atuacao{text-align:center;padding:3.4rem 0;border-bottom:1px solid rgba(157,180,204,.1)}
        .adv-atuacao .adv-sub{display:inline-block;padding-bottom:.8rem}
        .adv-atuacao .adv-sub::after{left:50%;transform:translateX(-50%)}
        .adv-atuacao p{color:#cdd2da;line-height:1.95;font-size:1.06rem;max-width:70ch;margin:1.4rem auto 0}
        /* CONTATO — padrão escuro da página, duas colunas (ref. Didier) */
        .adv-contato{padding:3.4rem 0 1rem}
        .adv-contato__h{text-align:center;color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.1em;font-size:clamp(1.15rem,2.6vw,1.5rem);margin:0 0 2rem;padding-bottom:.8rem;position:relative}
        .adv-contato__h::after{content:'';position:absolute;left:50%;transform:translateX(-50%);bottom:0;width:54px;height:3px;background:#d0835d;border-radius:2px}
        .adv-contato__grid{display:grid;grid-template-columns:1fr 1fr;gap:2.8rem;align-items:start}
        .adv-contato__info{color:#cdd2da;line-height:1.8}
        .adv-contato__info strong{display:block;font-size:1.05rem;margin:0 0 .55rem;color:#f3f4f6}
        .adv-contato__info address{font-style:normal;font-size:.99rem;margin:0 0 1.1rem}
        .adv-contato__info a{color:#9db4cc;text-decoration:none;font-weight:500}
        .adv-contato__info a:hover{color:#fff}
        .adv-contato__info .line{display:block;margin:.25rem 0}
        .adv-form{display:flex;flex-direction:column;gap:.25rem}
        .adv-form label{color:#9db4cc;font-size:.74rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;margin:.55rem 0 .25rem}
        .adv-form input,.adv-form textarea{font-family:'Montserrat',sans-serif;background:rgba(157,180,204,.06);border:1px solid rgba(157,180,204,.28);border-radius:4px;color:#eef1f5;font-size:.98rem;padding:.62rem .8rem;transition:border-color .18s ease,background .18s ease}
        .adv-form input:focus,.adv-form textarea:focus{outline:none;border-color:#d0835d;background:rgba(208,131,93,.07)}
        .adv-form textarea{min-height:110px;resize:vertical}
        .adv-form button{align-self:flex-start;margin-top:1.1rem;font-family:'Montserrat',sans-serif;font-weight:600;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:#0a0a0b;background:#d0835d;border:2px solid #d0835d;border-radius:0;padding:.72rem 2.1rem;cursor:pointer;transition:background .2s ease,color .2s ease}
        .adv-form button:hover{background:transparent;color:#d0835d}
        .adv-honey{display:none}
        @media(max-width:760px){.adv-cols{grid-template-columns:1fr;gap:2rem}.adv-contato__grid{grid-template-columns:1fr;gap:1.8rem}}
        </style>
        <div class="adv">

          <section class="adv-esc">
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-1.jpg')"></div>
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-2.jpg')"></div>
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-3.jpg')"></div>
            <div class="adv-esc__ov"></div>
            <div class="adv-esc__in">
              <div class="adv-esc__title">Consultoria jurídica</div>
              <div class="adv-cols">
                <div class="adv-cols__text">
                  <h2 class="adv-sub">Conheça o Escritório</h2>
                  <p>A sociedade teve início em <strong>2007</strong>, quando <strong>Sergio Cosmo</strong> e <strong>Carlo Cosentino</strong>, advogados desde 2000 e 2005, resolveram unir suas forças, constituindo, assim, o escritório <strong>Cosmo e Cosentino Advogados</strong>.</p>
                  <p>O escritório nasceu do ideal comum dos seus sócios fundadores em empreender uma advocacia voltada à defesa de interesses de pessoas físicas com a mesma atenção e profissionalismo comumente dedicados aos seus clientes empresariais.</p>
                  <p>O assessoramento às pessoas jurídicas ocorre tanto no contencioso judicial como na esfera consultiva, abrangendo empresas, organizações não governamentais e entidades de classe.</p>
                </div>
                <div class="adv-officecard">
                  <img class="adv-officecard__logo" src="/img/cosmo-brand-white.png" alt="Cosmo & Cosentino Advogados">
                  <p class="adv-officecard__desc">Atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor.</p>
                  <a class="adv-officecard__btn" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">Visite o site Cosmo e Cosentino Advogados</a>
                </div>
              </div>
            </div>
          </section>

          <section class="adv-atuacao">
            <h2 class="adv-sub">Área de atuação</h2>
            <p>Histórico de atuação na defesa dos interesses de pessoas físicas, empresas, organizações não governamentais e entidades de classe. Intensa experiência em demandas relacionadas ao terceiro setor e às relações individuais e coletivas de trabalho.</p>
          </section>

          <section class="adv-contato">
            <h2 class="adv-contato__h">Contato</h2>
            <div class="adv-contato__grid">
              <div class="adv-contato__info">
                <strong>Cosmo &amp; Cosentino Advogados</strong>
                <address>
                  Rua Frei Matias Teves, 280 — 305<br>
                  Ilha do Leite, Recife / PE
                </address>
                <a class="line" href="https://wa.me/5581996372619" target="_blank" rel="noopener">WhatsApp: (81) 99637-2619</a>
                <a class="line" href="tel:+558130330089">Telefone: (81) 3033-0089</a>
                <a class="line" href="mailto:contato@cosmocosentino.com">contato@cosmocosentino.com</a>
              </div>
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
            </div>
          </section>

        </div>
    design:
      columns: '1'
---
