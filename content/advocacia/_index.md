---
title: 'Consultoria Jurídica'
date: 2026-06-15
type: landing

sections:
  - block: markdown
    content:
      title: 'Consultoria Jurídica'
      text: |-
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
        .adv{font-family:'Montserrat',system-ui,sans-serif;position:relative;left:50%;transform:translateX(-50%);width:min(1040px,92vw)}
        /* SEÇÃO do escritório — fotos (rotativas) full-bleed ao fundo */
        .adv-esc{position:relative;width:100vw;margin-left:calc(50% - 50vw);overflow:hidden;padding:4rem 0}
        .adv-esc__slide{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;opacity:0;animation:advfade 18s infinite}
        .adv-esc__slide:nth-child(1){animation-delay:0s}
        .adv-esc__slide:nth-child(2){animation-delay:6s}
        .adv-esc__slide:nth-child(3){animation-delay:12s}
        @keyframes advfade{0%{opacity:0}2%{opacity:1}30%{opacity:1}34%{opacity:0}100%{opacity:0}}
        .adv-esc__ov{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(10,10,11,.82),rgba(10,10,11,.88))}
        .adv-esc__in{position:relative;z-index:2;max-width:1040px;margin:0 auto;padding:0 clamp(1.2rem,4vw,2.6rem)}
        /* Bloco "sobre" — logo centralizada + texto em duas colunas equilibradas */
        .adv-about{max-width:920px;margin:0 auto;text-align:center}
        .adv-about__logo{width:min(250px,72%);height:auto;display:inline-block;margin:0 0 2rem}
        .adv-about__cols{column-count:2;column-gap:3rem;text-align:left;margin:0}
        .adv-about__cols p{color:#e6eaef;line-height:1.85;font-size:1rem;margin:0 0 1.05rem;break-inside:avoid;text-shadow:0 1px 10px rgba(0,0,0,.45)}
        .adv-about__cols p:last-child{margin-bottom:0}
        .adv-about__link{display:inline-block;margin:2rem 0 0;font-weight:500;font-size:.95rem;letter-spacing:.02em;color:#fff;text-decoration:none;border-bottom:1px solid #d0835d;padding-bottom:.22rem;transition:border-color .2s ease}
        .adv-about__link:hover{border-color:#fff}
        @media(max-width:680px){.adv-about__cols{column-count:1}}
        /* Subtítulos de seção (cobre delicado) */
        .adv-sub{color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:clamp(1rem,1.9vw,1.15rem);margin:0 0 1.2rem;position:relative;padding-bottom:.75rem}
        .adv-sub::after{content:'';position:absolute;left:0;bottom:0;width:96px;height:1px;background:#d0835d}
        /* ÁREA DE ATUAÇÃO — alinhado à esquerda */
        .adv-atuacao{text-align:left;padding:3.4rem 0;border-bottom:1px solid rgba(157,180,204,.1)}
        .adv-atuacao p{color:#cdd2da;line-height:1.95;font-size:1.06rem;max-width:80ch;margin:1.3rem 0 0;text-align:left}
        /* CONTATO — padrão escuro, alinhado à esquerda, duas colunas */
        .adv-contato{padding:3.4rem 0 1rem}
        .adv-contato__h{text-align:left;color:#f3f4f6;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:clamp(1rem,1.9vw,1.15rem);margin:0 0 1.8rem;padding-bottom:.75rem;position:relative}
        .adv-contato__h::after{content:'';position:absolute;left:0;bottom:0;width:96px;height:1px;background:#d0835d}
        .adv-contato__grid{display:grid;grid-template-columns:1fr 1fr;gap:2.8rem;align-items:start}
        .adv-contato__info{color:#cdd2da;line-height:1.8}
        .adv-contato__info strong{display:block;font-size:1.05rem;margin:0 0 .55rem;color:#f3f4f6;font-weight:600}
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
        @media(max-width:760px){.adv-contato__grid{grid-template-columns:1fr;gap:1.8rem}}
        </style>
        <div class="adv">

          <section class="adv-esc">
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-1.jpg')"></div>
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-2.jpg')"></div>
            <div class="adv-esc__slide" style="background-image:url('/img/adv-slide-3.jpg')"></div>
            <div class="adv-esc__ov"></div>
            <div class="adv-esc__in">
              <div class="adv-about">
                <img class="adv-about__logo" src="/img/cosmo-brand-emblem-copper.png" alt="Cosmo & Cosentino Advogados">
                <div class="adv-about__cols">
                  <p>Cosmo e Cosentino Advogados foi fundado em 2007, a partir da união de Sergio Cosmo e Carlo Cosentino – advogados desde 2000 e 2005, respectivamente. A sociedade nasceu de um propósito compartilhado: exercer uma advocacia de excelência, que dedique às pessoas físicas a mesma atenção e o mesmo rigor profissional tradicionalmente reservados à clientela empresarial.</p>
                  <p>A atuação voltada às pessoas jurídicas – empresas, entidades de classe e sindicatos, além de organizações não governamentais e demais instituições do terceiro setor – desenvolve-se no contencioso judicial, na consultoria jurídica e na negociação coletiva trabalhista.</p>
                  <p>Compõe ainda o portfólio do escritório um serviço de cálculos judiciais, sobretudo trabalhistas, apoiado em sistema próprio de elaboração e auditoria, que confere precisão e previsibilidade à gestão do passivo.</p>
                </div>
                <a class="adv-about__link" href="https://www.cosmocosentino.com" target="_blank" rel="noopener">Visite o site</a>
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
