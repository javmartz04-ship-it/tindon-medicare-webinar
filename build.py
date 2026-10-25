# Build index.html from src.html: inline the traced Tindon logo and the review stars.
import re
svg=open('assets/tindon.svg').read()
var={'n':'var(--ln,#0B2950)','o':'var(--lo,#FF914D)','w':'var(--lw,#fff)'}
paths=re.sub(r'class="([now])"',lambda m:f'style="fill:{var[m.group(1)]}"',re.search(r'<svg[^>]*>(.*)</svg>',svg,re.S).group(1))
star='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6-4.9-4.6 6.6-.8z"/></svg>'
import os
A='assets/' if os.environ.get('LOCAL') else 'https://javmartz04-ship-it.github.io/tindon-medicare-webinar/assets/'
src=open('src.html').read().replace('{{A}}',A).replace('{{LOGO}}',paths).replace('{{STARS}}',star*5)
open('index.html','w').write(src)
open('thanks.html','w').write(open('thanks.src.html').read().replace('{{A}}',A).replace('{{LOGO}}',paths))
# favicon: shield mark only
fav=re.sub(r'class="([now])"',lambda m:'fill="'+{'n':'#0B2950','o':'#FF914D','w':'#fff'}[m.group(1)]+'"',re.search(r'<svg[^>]*>(.*)</svg>',svg,re.S).group(1))
open('assets/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="20 0 520 568">{fav}</svg>')
print(len(src))
