# Tramia — landing page

## Publicar (Netlify, ~5 min)
1. Acesse app.netlify.com → Add new site → **Deploy manually**.
2. Arraste esta pasta `tramia-landing` inteira (não o zip, a pasta descompactada).
3. Site settings → Change site name → `tramia` (fica `tramia.netlify.app`, se livre).
4. Forms → **Enable form detection** → faça um novo deploy (arraste a pasta de novo).
5. Forms → Notifications → **Email notification** → tramia.integra@gmail.com.
6. Teste pelo celular, no endereço `https://...netlify.app` (não abrindo o arquivo local): preencha, marque o consentimento e envie. O lead aparece em Forms → diagnostico.

## Importante
O envio só funciona hospedado no Netlify. Abrindo o `index.html` do computador, ou em outro host, sempre aparece a tela de falha com o botão do WhatsApp.

## Se o envio falhar
O formulário oferece abrir o WhatsApp já preenchido com os dados digitados. Nenhum contato se perde.

## Campos coletados (Netlify Forms)
nome, empresa, whatsapp, sistemas (opcional), dor (opcional), consentimento (checkbox LGPD, obrigatório).

## Retenção
Prazo definido: 12 meses (citado na nota de privacidade). Apague os leads antigos em Forms → diagnostico.

## Estrutura
- index.html — página única (HTML + CSS + JS, sem dependências)
- img/ — ilustrações em WebP (~90 KB no total)
