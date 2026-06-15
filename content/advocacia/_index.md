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
        /* HERO — carrossel de fotos (como na home do cosmocosentino.com) com o título "Consultoria jurídica" */
        .adv-slider{position:relative;border-radius:10px;overflow:hidden;aspect-ratio:1600/703;box-shadow:0 30px 70px -34px rgba(0,0,0,.95);border:1px solid rgba(157,180,204,.18)}
        .adv-slide{position:absolute;inset:0;background-size:cover;background-position:center;opacity:0;animation:advfade 18s infinite}
        .adv-slide:nth-child(1){animation-delay:0s}
        .adv-slide:nth-child(2){animation-delay:6s}
        .adv-slide:nth-child(3){animation-delay:12s}
        @keyframes advfade{0%{opacity:0}2%{opacity:1}30%{opacity:1}34%{opacity:0}100%{opacity:0}}
        .adv-slider__title{position:absolute;left:0;right:0;bottom:0;z-index:2;padding:2.6rem 1.6rem 1.4rem;background:linear-gradient(to top,rgba(10,10,11,.82),rgba(10,10,11,.25) 60%,transparent);color:#fff;text-align:center;font-weight:600;text-transform:uppercase;letter-spacing:.16em;font-size:clamp(1.1rem,2.6vw,1.7rem)}
        /* Seção dois blocos: texto à esquerda, cartão do escritório à direita */
        .adv-block{padding:3.4rem 0;border-bottom:1px solid rgba(157,180,204,.1)}
        .adv-block:last-child{border-bottom:0;padding-bottom:1rem}
        .adv-sub{color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:clamp(1.1rem,2.4vw,1.45rem);margin:0 0 1.3rem;position:relative;padding-bottom:.7rem}
        .adv-sub::after{content:'';position:absolute;left:0;bottom:0;width:52px;height:3px;background:#d0835d;border-radius:2px}
        .adv-cols{display:grid;grid-template-columns:1.05fr .95fr;gap:2.8rem;align-items:center}
        .adv-cols__text p{color:#cdd2da;line-height:1.9;font-size:1.02rem;text-align:left;margin:0 0 1.05rem}
        .adv-cols__text p:last-child{margin-bottom:0}
        .adv-cols__text strong{color:#f3f4f6;font-weight:600}
        /* Cartão claro do escritório (logo + texto + visite o site) */
        .adv-card{background:#fff;border:1px solid #e6e4e0;border-top:4px solid #d0835d;border-radius:3px;padding:2.4rem 1.9rem;text-align:center;box-shadow:0 26px 60px -32px rgba(0,0,0,.9)}
        .adv-card__logo{width:min(250px,80%);height:auto;display:block;margin:0 auto 1.4rem}
        .adv-card__desc{color:#495057;font-size:.96rem;line-height:1.65;margin:0 0 1.6rem}
        .adv-card__btn{display:inline-block;font-weight:600;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:#d0835d;border:2px solid #d0835d;border-radius:0;padding:.7rem 1.6rem;text-decoration:none;transition:background .2s ease,color .2s ease}
        .adv-card__btn:hover{background:#d0835d;color:#fff}
        /* Área de atuação */
        .adv-atuacao{text-align:center}
        .adv-atuacao .adv-sub{display:inline-block;padding-bottom:.8rem}
        .adv-atuacao .adv-sub::after{left:50%;transform:translateX(-50%)}
        .adv-atuacao p{color:#cdd2da;line-height:1.95;font-size:1.06rem;max-width:70ch;margin:1.4rem auto 0}
        /* CONTATO — faixa na cor da paleta do site (#9db4cc), duas colunas (ref. Didier) */
        .adv-contato{background:#9db4cc;border-radius:4px;margin-top:3.4rem;padding:2.9rem 2.3rem}
        .adv-contato__h{text-align:center;color:#0a0a0b;font-weight:700;text-transform:uppercase;letter-spacing:.12em;font-size:1.4rem;margin:0 0 2rem;padding-bottom:.8rem;position:relative}
        .adv-contato__h::after{content:'';position:absolute;left:50%;transform:translateX(-50%);bottom:0;width:52px;height:3px;background:#0a0a0b;opacity:.55;border-radius:2px}
        .adv-contato__grid{display:grid;grid-template-columns:1fr 1fr;gap:2.6rem;align-items:start}
        .adv-contato__info{color:#10243a}
        .adv-contato__info strong{display:block;font-size:1.05rem;margin:0 0 .55rem;color:#0a0a0b}
        .adv-contato__info address{font-style:normal;line-height:1.8;font-size:.98rem;margin:0 0 1.1rem}
        .adv-contato__info a{color:#10243a;text-decoration:none;font-weight:500}
        .adv-contato__info a:hover{color:#0a0a0b;text-decoration:underline}
        .adv-contato__info .line{display:block;margin:.2rem 0}
        .adv-form{display:flex;flex-direction:column;gap:.25rem}
        .adv-form label{color:#10243a;font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin:.55rem 0 .25rem}
        .adv-form input,.adv-form textarea{font-family:'Montserrat',sans-serif;background:#fff;border:1px solid rgba(10,10,11,.18);border-radius:4px;color:#0a0a0b;font-size:.98rem;padding:.62rem .8rem}
        .adv-form input:focus,.adv-form textarea:focus{outline:none;border-color:#d0835d;box-shadow:0 0 0 2px rgba(208,131,93,.25)}
        .adv-form textarea{min-height:110px;resize:vertical}
        .adv-form button{align-self:flex-start;margin-top:1.1rem;font-family:'Montserrat',sans-serif;font-weight:700;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:#0a0a0b;border:2px solid #0a0a0b;border-radius:0;padding:.72rem 2.1rem;cursor:pointer;transition:background .2s ease,color .2s ease}
        .adv-form button:hover{background:transparent;color:#0a0a0b}
        .adv-honey{display:none}
        @media(max-width:760px){.adv-cols{grid-template-columns:1fr;gap:2rem}.adv-contato__grid{grid-template-columns:1fr;gap:1.8rem}}
        </style>
        <div class="adv">

          <div class="adv-slider">
            <div class="adv-slide" style="background-image:url('/img/adv-slide-1.jpg')"></div>
            <div class="adv-slide" style="background-image:url('/img/adv-slide-2.jpg')"></div>
            <div class="adv-slide" style="background-image:url('/img/adv-slide-3.jpg')"></div>
            <div class="adv-slider__title">Consultoria jurídica</div>
          </div>

          <section class="adv-block">
            <div class="adv-cols">
              <div class="adv-cols__text">
                <h2 class="adv-sub">Conheça o Escritório</h2>
                <p>A sociedade teve início em <strong>2007</strong>, quando <strong>Sergio Cosmo</strong> e <strong>Carlo Cosentino</strong>, advogados desde 2000 e 2005, resolveram unir suas forças, constituindo, assim, o escritório <strong>Cosmo e Cosentino Advogados</strong>.</p>
                <p>O escritório nasceu do ideal comum dos seus sócios fundadores em empreender uma advocacia voltada à defesa de interesses de pessoas físicas com a mesma atenção e profissionalismo comumente dedicados aos seus clientes empresariais.</p>
                <p>O assessoramento às pessoas jurídicas ocorre tanto no contencioso judicial como na esfera consultiva, abrangendo empresas, organizações não governamentais e entidades de classe.</p>
              </div>
              <div class="adv-card">
                <img class="adv-card__logo" src="/img/cosmo-consentino-brand.png" alt="Cosmo & Cosentino Advogados">
                <p class="adv-card__desc">Atuação consultiva e contenciosa em Direito do Trabalho, Direito Sindical e Terceiro Setor.</p>
                <a class="adv-card__btn" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">Visite o site Cosmo e Cosentino Advogados</a>
              </div>
            </div>
          </section>

          <section class="adv-block adv-atuacao">
            <h2 class="adv-sub">Área de atuação</h2>
            <p>Histórico de atuação na defesa dos interesses de pessoas físicas, empresas, organizações não governamentais e entidades de classe. Intensa experiência em demandas relacionadas ao terceiro setor e às relações individuais e coletivas de trabalho.</p>
          </section>

          <div class="adv-contato">
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
          </div>

        </div>
    design:
      columns: '1'
---
