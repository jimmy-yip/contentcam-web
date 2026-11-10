#!/bin/bash
# Downloads Apple's official localized "Download on the App Store" badges (black SVG) for each site language.
# Run by Jimmy (the agent sandbox can't reach tools.applemarketingtools.com):  bash ~/contentcam-web/tools/fetch-apple-badges.sh
out=~/contentcam-web/assets/badges; mkdir -p "$out"
for p in de:de-de es:es-mx fr:fr-fr it:it-it ja:ja-jp pt-br:pt-br id:id-id ko:ko-kr nl:nl-nl pl:pl-pl tr:tr-tr vi:vi-vn \
         zh-hans:zh-cn zh-hant:zh-tw ru:ru-ru hi:hi-in sv:sv-se th:th-th ms:ms-my da:da-dk no:nb-no fi:fi-fi \
         pt-pt:pt-pt uk:uk-ua fil:fil-ph bn:bn-in cs:cs-cz ro:ro-ro hu:hu-hu el:el-gr; do
  d=${p%%:*}; a=${p##*:}
  if curl -sfL -m 20 -o "$out/app-store-$d.svg" "https://tools.applemarketingtools.com/api/badges/download-on-the-app-store/black/$a?size=250x83"; then
    echo "ok   $d ($a)"; else rm -f "$out/app-store-$d.svg"; echo "none $d ($a)"; fi
done
