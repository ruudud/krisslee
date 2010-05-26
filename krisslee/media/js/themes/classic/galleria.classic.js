Galleria.themes.create({
    name: 'classic',
    author: 'Galleria',
    version: '1.0',
    css: 'galleria.classic.css',
    defaults: {
        transition: 'slide'
    },
    init: function(options) {
        
        var mc = Galleria.MAC && Galleria.CHROME;
        
        if (!mc) {
            this.$('thumbnails').children().hover(function() {
                $(this).not('.active').fadeTo(200, .4);
            }, function() {
                $(this).fadeTo(400, 1);
            });
        }
        
        this.$('container').height(this.stageHeight = ( this.options.height || Math.round(this.stageWidth*9/16) ));
        this.rescale();
        this.$('loader').show().fadeTo(200, 0.4);
        this.$('counter').show().fadeTo(200, 0.4);
       
        var playing = true;
 
        this.$('container').hover(this.proxy(function() {
            this.$('image-nav-left,image-nav-right').fadeIn(200);
            this.pause();
            playing = false;
        }), this.proxy(function() {
            this.$('image-nav-left,image-nav-right').fadeOut(500);
            this.play(5000);
            playing = true;
        }));
        
        this.$('image-nav-left,image-nav-right').hide();
        this.$('counter').show();
        
        this.$('stage').hover(
            this.proxy(function() {this.pause();}),
            this.proxy(function() {this.play(5000);})
        );
       
        this.attachKeyboard({
            74: this.prev, //j
            75: this.next, //k
            32: function() { //space
                if (playing) {
                    this.pause();
                    playing = false;
                }
                else {
                    this.play(5000);
                    playing = true;
                }
            }
        });
        
        this.bind(Galleria.LOADSTART, function(e) {
            if (!e.cached) {
                this.$('loader').show().fadeTo(200, .4);
            }
            if (this.hasInfo()) {
                this.$('info').show();
                this.$('info-text').show();
                this.$('info-link').hide();
                this.$('info-close').hide();
            } else {
                this.$('info-text').hide();
                this.$('info').hide();
            }
            if (!mc) {
                $(e.thumbTarget).parent().css('opacity',1).addClass('active').siblings().removeClass('active');
            }
        });

        this.bind(Galleria.LOADFINISH, function(e) {
            this.$('loader').fadeOut(200);
        });

        this.play(5000);
        
        this.show(0);
    }
});
