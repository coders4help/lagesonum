% include('views/header.tpl', active='about')

<div class="container">
      <div class="starter-template">

<h3>{{_(u'about_link')}}</h3>

<p>{{_(u'about_par1')}}</p>
<p>{{_(u'about_par2')}}</p>
<p>{{_(u'about_par3')}}</p>
<p><a href="http://www.taz.de/Wartezeiten-am-Berliner-Lageso/!5228958/">{{_(u'tazlink')}}</a></p>

<h2>{{_('pressrelease_heading')}}</h2>
<a href="pm-start" target="_blank">{{_('pm_start')}}</a>

      </div>
</div>

<div align="center">
<a class="twitter-timeline"  href="https://twitter.com/lagesonum" data-widget-id="648776089519702016">Tweets von @lagesonum </a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>



% include('views/footer.tpl')
