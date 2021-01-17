alert(/^http?/.test('https'));

alert(/\w+\.jpe?g/.test('image.jpeg'));

alert(/\d{1,12}/.test('7312347'));

alert(/^\d{1,2}.\d{1,2}.\d{4}/.test('22.02.2222'));

alert(/(^[^.][a-z\d._-]+[^.])@([a-z]{4})\.([a-z]{2,3})/.test('hello@mail.ru'))