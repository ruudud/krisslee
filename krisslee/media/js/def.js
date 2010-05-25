/** Holding variables **/
//Jiggle containers
var timers = new Array();
var dir = 0;
var current_obj;

$(document).ready(function() {
    /** Count-down init **/
    var lee_date = new Date(2010, 6, 1, 0, 0);
    
    if ((new Date()).getTime() < lee_date) {
        $('#countdown').countdown({
                alwaysExpire: true,
                until: lee_date,
                compact: true,
                layout:'Slapp av, det er bare <br/><span>{dn}</span>d <span>{hnn}</span>t <span>{mnn}</span>m <span>{snn}</span>s igjen.'
            });
    }

    /** Jiggle init **/
    jiggle('#regImg');
    

});

function jiggle(selector) {
    $(selector).mouseover(function() {
        padd(selector, 0);
    });
    $(selector).mouseout(function() {
        for (var i=0; i<timers.length; i++) {
            //Even if we have more jiggles, only one moves at a time.
            clearInterval(timers[i]);
        }
        $(this).removeClass();
        $(this).addClass('padd_3');
    });

}

function padd(selector, new_dir) {
    $(selector).removeClass();
    $(selector).addClass('padd_' + dir);

    //TODO: Find a better way than the use of containers.
    current_obj = selector;
    dir = new_dir + 1;
    if (dir == 4) {
        dir = 0;
    }
    timers[timers.length] = window.setTimeout('padd(current_obj, dir)', 200);
}
