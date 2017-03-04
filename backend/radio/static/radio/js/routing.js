serverURL = 'localhost:8000';

var root = 'http://xray';
var useHash = false;
var router = new Navigo(root, useHash);
console.log("Working");

router.on({
  '/live': function () {
    alert('Live !');
  },
})
.resolve();
