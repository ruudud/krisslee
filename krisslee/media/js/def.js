/** Count-down init **/
$(function() {
  var lee_date = new Date(2010, 6, 1, 0, 0);
  
  if ((new Date()).getTime() < lee_date) {
      $('#countdown').countdown({
              alwaysExpire: true,
              until: lee_date,
              compact: true,
              layout:'Slapp av, bare <br/><span>{dn}</span>d <span>{hnn}</span>t <span>{mnn}</span>m <span>{snn}</span>s igjen.'
          });
  }
});
