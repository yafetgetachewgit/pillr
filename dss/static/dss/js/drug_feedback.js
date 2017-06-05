function createDonut(d3, dataset, elem) {
    'use strict';


    var width = 380;
    var height = 240;
    var radius = Math.min(width, height) / 2;
    var donutWidth = 50;
    var legendRectSize = 18;                                  // NEW
    var legendSpacing = 4;                                    // NEW

    var color = d3.scale.category20b();

    var svg = d3.select(elem)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(' + (radius) +
        ',' + (height / 2) + ')');

    var arc = d3.svg.arc()
        .innerRadius(radius - donutWidth)
        .outerRadius(radius);

    var pie = d3.layout.pie()
        .value(function (d) {
            return d.count;
        })
        .sort(null);

    var path = svg.selectAll('path')
        .data(pie(dataset[1]))
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function (d, i) {
            return color(d.data.label);
        });

    var legend = svg.selectAll('.legend')
        .data(color.domain())
        .enter()
        .append('g')
        .attr('class', 'legend')
        .attr('transform', function (d, i) {
            var height = legendRectSize + legendSpacing;
            var offset = height * color.domain().length / 2;     // NEW
            var horz = radius+10;                       // NEW
            var vert = i * height - offset;                       // NEW
            return 'translate(' + horz + ',' + vert + ')';        // NEW
        });                                                     // NEW


    legend.append('rect')                                     // NEW
        .attr('width', legendRectSize)                          // NEW
        .attr('height', legendRectSize)                         // NEW
        .style('fill', color)                                   // NEW
        .style('stroke', color);                                // NEW

    legend.append('text')                                     // NEW
        .attr('x', legendRectSize + legendSpacing)              // NEW
        .attr('y', legendRectSize - legendSpacing)              // NEW
        .text(function (d) {
            return d;
        });                       // NEW



}



(function(d3){






    //alert(drug_responses['Netilmicin']);
    //
    //data = JSON.parse(drug_responses);
    //
    //alert(data);



    var dataset = [
        [
            {drug_name: 'amoxillin'}
        ],
        [
            {label: 'Feeling Better', count: 10},
            {label: 'No Change', count: 20},
            {label: 'Feeling Worse', count: 30}
        ]
    ];

    elem = "#chart";
    i = 0;
    for (d in drug_responses){
        dataset[0][0].drug_name = d;
        dataset[1][0].count = drug_responses[d].better;
        dataset[1][1].count = drug_responses[d].same;
        dataset[1][2].count = drug_responses[d].worse;
        $("#charts_drug_feedback").append("<div class='chart' id='chart"+i+"'><p>"+d+"</p></div>");
        createDonut(d3, dataset,elem+i);
        i++;
    }



})(window.d3);