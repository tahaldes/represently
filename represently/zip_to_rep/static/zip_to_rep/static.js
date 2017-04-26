module('magicTricks', {
    beforeEach: function() {
        var $ = django.jQuery;
        $('#qunit-fixture').append('<button class="button"></button>');
    }
});

test('removeOnClick removes button on click', function(assert) {
    var $ = django.jQuery;
    removeOnClick('.button');
    assert.equal($('.button').length === 1);
    $('.button').click();
    assert.equal($('.button').length === 0);
});

test('copyOnClick adds button on click', function(assert) {
    var $ = django.jQuery;
    copyOnClick('.button');
    assert.equal($('.button').length === 1);
    $('.button').click();
    assert.equal($('.button').length === 2);
});