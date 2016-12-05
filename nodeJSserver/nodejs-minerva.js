const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;

var Minerva = require('mcgill-minerva-api');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
	
	var body = [];
  req.on('error', function(err) {
    console.error(err);
  }).on('data', function(chunk) {
    body.push(chunk);
  }).on('end', function() {
    body = Buffer.concat(body).toString();
		var parsed = JSON.parse(body);
		var user = parsed['username'];
		var pass = parsed['password'];

		var minerva = new Minerva(user, pass);
		minerva.getTranscript().then(function(tr){

			var courses = new Array();
			for(i = 0; i < tr.length; i++) {
				var g = tr[i].grade;

				if(g == 'A' || g == 'A-' || g == 'B+' || g == 'B-' || g == 'B' || g == 'C+' || g == 'C' || g == 'D' || g == 'F') {
					var scode = tr[i].course_number;	
					if(scode.length > 4)
						scode = scode.substr(0,5);

					var x = {subject: tr[i].department, code: scode, grade:g};
					courses.push(x);
				}
			}

			res.end(JSON.stringify(courses));
		});
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
