rm precache-manifest* ; npm run build && cp -rp build/* . && sed -i "s%=\"/static%=\"/patalog/static%g" ./index.html && git add -A && git commit -a && git push