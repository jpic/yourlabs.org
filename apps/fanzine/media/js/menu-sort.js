jQuery(function($) {
    $("div.inline-group").sortable({ 
        //axis: 'y',
        placeholder: 'ui-state-highlight', 
        forcePlaceholderSize: 'true', 
        items: 'div.inline-related', 
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('input[id$=id]').val()) {
                    $(this).find('input[id$=order]').val(i+1);
                }
        });
        }
    });
    $("div.inline-group").disableSelection();

});

jQuery(document).ready(function($){
    $(this).find('input[id$=order]').parent('div').parent('div').hide().parent().parent().css('cursor','move');
});



/* credit: http://djangosnippets.org/snippets/1053/ */
