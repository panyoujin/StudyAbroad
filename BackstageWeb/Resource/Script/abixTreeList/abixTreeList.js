/*
 * abixTreeList jQuery plugin.
 *
 * Author: Dariusz Walega | darek@abix.com.pl, www.abix.com.pl, www.abix.pl
 *
 * Written using boilerplate code from
 * http://coding.smashingmagazine.com/2011/10/11/essential-jquery-plugin-patterns/
 *
 * MIT License. 
 * 
 */

;(function($, window, document, undefined) {
    
    var pluginName = 'abixTreeList',
        defaults = {
            collapsedIconClass  : 'fa-plus',
            expandedIconClass   : 'fa-minus'
        };

    function Plugin(element, options) {
        this.element    = element;
        this.$element   = $(element);
        this.options    = $.extend({}, defaults, options);
        this._defaults  = defaults;
        this._name      = pluginName,
        this.$topLevelBranches,
        this.$allBranches,
        this.init();
    }

    Plugin.prototype.init = function() {
        var self                = this;
        self.$topLevelBranches  = self.$element.children('li');
        self.$allBranches       = self.$element.find('li');
        
        self.$element.addClass('abix-tree-list');
        self.$allBranches.not(self.$topLevelBranches).hide();
        self.$allBranches.each(function() {
            var $children = $(this).children('ul,ol');
            if ($children.size() > 0) {
                $(this).addClass('collapsed');
                $('<span class="icon"><i class="fa ' + self.options.collapsedIconClass + '"></i></span>').prependTo($(this));
            }else {
                $('<span style="display:inline-block;width:23px;"></span>').prependTo($(this));
            }
        });

        if (self.options.expandAll) {
            self.expandAll();
        }
        
        self.$allBranches.children('span.icon').on('click', function(e) {
            if ($(this).parent().hasClass('collapsed')) {
                self.expand($(this).parent());
                e.stopPropagation();
            }
            if ($(this).parent().hasClass('expanded')) {
                self.collapse($(this).parent());
                e.stopPropagation();
            }
        });
        
        $('#tree-expand-all').on('click', function(e) {
            e.preventDefault();
            self.expandAll();
            e.stopPropagation();
        });
        
        $('#tree-collapse-all').on('click', function(e) {
            e.preventDefault();
            self.collapseAll();
            e.stopPropagation();
        });
    };
    
    Plugin.prototype.expand = function($branch) {
        var self = this;
        $branch.children('ul,ol').children('li').show(120, function() {
            $branch.removeClass('collapsed').addClass('expanded');
            $branch.children('span.icon').children("i").removeClass(self.options.collapsedIconClass).addClass(self.options.expandedIconClass);
        });
    };
    
    Plugin.prototype.collapse = function($branch) {
        var self = this;
        $branch.children('ul,ol').children('li').hide(120, function() {
            $branch.removeClass('expanded').addClass('collapsed');
            $branch.children('span.icon').children("i").removeClass(self.options.expandedIconClass).addClass(self.options.collapsedIconClass);
        });
    };
    
    Plugin.prototype.collapseAll = function() {
        var self = this;
        self.$allBranches.not(self.$topLevelBranches).hide(120, function() {
            self.$allBranches.removeClass('expanded').addClass('collapsed');
            self.$allBranches.children('span.icon').children("i").removeClass(self.options.expandedIconClass).addClass(self.options.collapsedIconClass);
        });    
    };
    
    Plugin.prototype.expandAll = function() {
        var self = this;
        self.$allBranches.show(1, function() {
            self.$allBranches.removeClass('collapsed').addClass('expanded');
            self.$allBranches.children('span.icon').children("i").removeClass(self.options.collapsedIconClass).addClass(self.options.expandedIconClass);
        });
    };
    
    $.fn[pluginName] = function (options) {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + pluginName)) {
                $.data(this, 'plugin_' + pluginName, 
                new Plugin(this, options));
            }
        });
    };

})(jQuery, window, document);