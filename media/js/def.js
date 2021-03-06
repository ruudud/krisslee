$(document).ready(function() {
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

            play_track(0);
            update_playing(0);
        }
        else {
            $('#nohtml5').show();
        }
    }
});

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

/** Media Player **/
function update_playing(t) {
    var file = songs[t];
    var cover = $('#cover');
    var t_info = $('#track_info');

    t_info.children('p').html(file.info);

    if (file.video) {
        t_info.css('width', '40%');
        cover.hide();

        t_info.children('p').prepend('<strong>' + file.artist + ' - ' + file.title + '</strong><br/>');
        //$('#now_playing').hide();
        //$('#poster').attr('src', file.image);
        //$('#poster').attr('alt', file.artist + ' - ' + file.title);
    }
    else {
        t_info.css('width', '50%');
        cover.hide();
        $('#track_artist').html(file.artist);
        $('#track_title').html(file.title);
        $('#cover').css('background-image', 'url("' + file.image + '")');
        cover.show();
    }
}

function play_track(t) {
    var apl = document.getElementById('aud_player');
    var vpl = document.getElementById('vid_player');
    var acont = $('#aud_cont');
    var vcont = $('#vid_cont');

    var file = songs[t];
    var pl;

    if (file.video) {
        apl.pause();
        acont.hide();

        vcont.show();
        pl = vpl;
    }
    else {
        vpl.pause();
        vcont.hide();

        acont.show();
        pl = apl;

        pl.src = 'http://www.palfashion.no/media/' + file.source;
    }

    pl.load();
    pl.play();
}
