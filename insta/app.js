var ig = require('instagram-scraping');
 const fs = require('fs');

// // ig.scrapeTag('veranda').then(result => {
// //   console.dir(result);
// // });

// // ig.deepScrapeTagPage('veranda').then(result => {
// //   console.dir(result);
// // });


ig.scrapeUserPage('mahi7781').then(result => {
  console.dir(result);
  fs.writeFileSync('result.json', JSON.stringify(result));

});



// fb
