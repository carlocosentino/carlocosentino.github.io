---
title: 'Contato'
date: 2026-06-04
type: landing

sections:
  - block: markdown
    content:
      title: 'Contato'
      text: |-
        <style>
        .site-contato--page{grid-template-columns:1fr!important;width:min(560px,92vw)!important;gap:1.6rem!important;padding-top:0}
        .site-contato--page form{align-items:stretch}
        .site-contato--page label{text-align:left}
        .site-contato--page button{align-self:center}
        .site-contato--page .site-contato__info{text-align:center}
        </style>
        <div class="site-contato site-contato--page">
        <div class="site-contato__form">
        <form action="https://formsubmit.co/contato@carlocosentino.com.br" method="POST">
        <input type="hidden" name="_subject" value="Contato pelo site – carlocosentino.com.br">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_next" value="https://www.carlocosentino.com.br/contato/?enviado=1">
        <input type="text" name="_honey" style="display:none">
        <label for="ct-nome">Seu nome</label>
        <input id="ct-nome" name="Nome" type="text" required>
        <label for="ct-email">Seu e-mail</label>
        <input id="ct-email" name="E-mail" type="email" required>
        <label for="ct-assunto">Assunto</label>
        <input id="ct-assunto" name="Assunto" type="text">
        <label for="ct-msg">Sua mensagem</label>
        <textarea id="ct-msg" name="Mensagem"></textarea>
        <button type="submit">ENVIAR</button>
        </form>
        </div>
        <div class="site-contato__info">
        <a class="wa" href="https://wa.me/5581996372619" target="_blank" rel="noopener">Falar no WhatsApp</a>
        </div>
        </div>
    design:
      columns: '1'
---
