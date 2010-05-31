/** Holding variables **/
//Jiggle containers
var timers = new Array();
var dir = 0;
var current_obj;

$(document).ready(function() {
    /** Menu **/
    $('#menu li').click(function(){
        location.href = $(this).children('span').children('a').attr('href');
    });
    $('#menu li').mouseover(function(){
        $(this).children('span').children('a').css({'color': '#000'});
    });
    $('#menu li').mouseout(function(){
        $(this).children('span').children('a').css({'color': '#FFF'});
    });

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

    /** Jukebox init **/
    if ($('#jukebox').length) {
        if (!!document.createElement('audio').canPlayType) {
            $('#jukebox').show();
            $('#jukebox li').click(function(){
                $('#jukebox li').removeClass('bold'); 
                $(this).addClass('bold');
                var id = $('#jukebox li').index($(this));
                play_track(id);
                update_playing(id);
            });
            update_playing(0);
        }
        else {
            $('#nohtml5').show();
        }
    }
});

function update_playing(t) {
    $('#track_artist').html(songs[t].artist);
    $('#track_title').html(songs[t].title);
    $('#track_info').html(songs[t].info);
    $('#cover').css('background-image', 'url("' + songs[t].image + '")');
}

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
(function($) {

	$.fn.konami = function(callback, code) {
		if(code == undefined) code = "38,38,40,40,37,39,37,39,66,65";
		
		return this.each(function() {
			var kkeys = [];
			$(this).keydown(function(e){
				kkeys.push( e.keyCode );
				if ( kkeys.toString().indexOf( code ) >= 0 ){
					$(this).unbind('keydown', arguments.callee);
					callback(e);
				}
			}, true);
		});
	}

})(jQuery);

/** Audio Player **/
function play_track(t) {
    var pl = document.getElementById('player');
    pl.pause();

    var track = songs[t].source;
    pl.src = 'http://www.palfashion.no/media/' + track;
    pl.load();
    pl.play();
}
