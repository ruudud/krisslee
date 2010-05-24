/** Holding variables **/

var timers = new Array();
var dir = 0;

/** Count-down init **/
$(function() {
    var lee_date = new Date(2010, 6, 1, 0, 0);
    
    if ((new Date()).getTime() < lee_date) {
        $('#countdown').countdown({
                alwaysExpire: true,
                until: lee_date,
                compact: true,
                layout:'Slapp av, det er bare <br/><span>{dn}</span>d <span>{hnn}</span>t <span>{mnn}</span>m <span>{snn}</span>s igjen.'
            });
    }

    $('#regImg').mouseover(function() {
        padd(0);
    });
    $('#regImg').mouseout(function() {
        for (var i=0; i<timers.length; i++) {
            clearInterval(timers[i]);
        }
        $(this).removeClass();
        $(this).addClass('padd_3');
    });
});

function padd(new_dir) {
    $('#regImg').removeClass();
    $('#regImg').addClass('padd_' + dir);
    dir = new_dir + 1;
    if (dir == 4) {
        dir = 0;
    }
    timers[timers.length] = window.setTimeout('padd(dir)', 200);
}
