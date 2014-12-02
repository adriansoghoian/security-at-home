$(document).ready(function() {


var yo = function() {
  $.ajax({
    url: "http://127.0.0.1:9393/testjson",
    type: "post",
    dataType: "json",
    data: { message: "Hello, I'm a message!!!!" },
    success: function(data) { console.log("Testing testing"); }
  });
}

yo();

nodes = [
{"name":"Router","group":1, rad:50, l_rad:60, x:400, y:200, fixed: true},
{"name":"Fridge","group":2, rad:5, l_rad:6},
{"name":"Webcam","group":3, rad:10, l_rad:12},
{"name":"Chromecast","group":3, rad:10,l_rad:12},
{"name":"Printer","group":3, rad:10, l_rad:12},
{"name":"iPhone","group":4, rad:15,l_rad:18},
{"name":"Desktop","group":4, rad:15,l_rad:18},
{"name":"iPad","group":4, rad:15,l_rad:18},
{"name":"Laptop","group":4, rad:15,l_rad:18},
{"name":"Lock","group":5, rad:5, l_rad:6},
{"name":"Cooker","group":5, rad:5, l_rad:6},
{"name":"Stereo","group":5, rad:5, l_rad:6},
{"name":"TV","group":5, rad:5, l_rad:6}
];

links = [
  {"source":0,"target":1,"value":1, "length":150},
  {"source":0,"target":2,"value":1, "length":100},
  {"source":0,"target":3,"value":1, "length":170},
  {"source":0,"target":4,"value":1, "length":170},
  {"source":0,"target":5,"value":1, "length":125},
  {"source":0,"target":6,"value":1, "length":175},
  {"source":0,"target":7,"value":1, "length":150},
  {"source":0,"target":8,"value":1, "length":100},
  {"source":0,"target":9,"value":1, "length":150},
  {"source":0,"target":10,"value":1, "length":150},
  {"source":0,"target":11,"value":1, "length":150},
  {"source":0,"target":12,"value":1, "length":150},
  {"source":2,"target":3,"value":0, "length":50},
  {"source":2,"target":4,"value":0, "length":50},
  {"source":3,"target":4,"value":0, "length":50},
  {"source":5,"target":6,"value":0, "length":50},
  {"source":6,"target":7,"value":0, "length":50},
  {"source":7,"target":8,"value":0, "length":50},
  {"source":5,"target":7,"value":0, "length":50},
  {"source":5,"target":8,"value":0, "length":50},
  {"source":6,"target":8,"value":0, "length":50},
  {"source":9,"target":10,"value":0, "length":30},
  {"source":9,"target":11,"value":0, "length":30},
  {"source":9,"target":12,"value":0, "length":30},
  {"source":10,"target":11,"value":0, "length":30},
  {"source":10,"target":12,"value":0, "length":30},
  {"source":11,"target":12,"value":0, "length":30},
  {"source":2,"target":4,"value":0, "length":50},
  {"source":4,"target":8,"value":0, "length":50},
  {"source":8,"target":11,"value":0, "length":300},
  {"source":11,"target":12,"value":0, "length":300}
];

var w = 800,
    h = 400;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-500)
    .linkDistance(30)
    .size([w, h])
    .nodes(nodes)
    .links(links)
    .linkDistance(function(d) {return d.length;})
    .start();

var svg = d3.select("body").append("svg")
  .attr("width", w)
  .attr("height", h);

var link = svg.selectAll(".link")
    .data(links)
  .enter().append("line")
    .attr("class", "link")
    .style("stroke-width", function(d) { return d.value; });

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function (d) {
  return  d.name + "";
})
svg.call(tip);

var node = svg.selectAll(".node")
    .data(nodes)
    .enter().append("circle")
    .attr("class", "node")
    .attr("r", function(d){return d.rad;})
    .style("fill", function(d) { return color(d.group); })
    .call(force.drag)
    //.on('mouseover', tip.show) 
    .on("mouseover", enlarge)
    //.on('mouseout', tip.hide)
    .on("mouseout", shrink); 

function enlarge() {
  console.log("Hello");
  d3.select(this).transition()
      .duration(750)
      .attr("r", function(d){return d.l_rad;});
}

function shrink() {
  d3.select(this).transition()
      .duration(750)
      .attr("r", function(d){return d.rad;});
}

node.append("title")
    .text(function(d) { return d.name; });

force.on("tick", function() {
  link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  node.attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
});

});
