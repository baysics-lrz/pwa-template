var ctx = document.getElementById('myObsChart').getContext('2d');
	var options= {
		responsive: true,
		indexAxis: 'y',
		scales: {
			xAxes: [{
				ticks: {
					beginAtZero: true,
					stepSize: 1
				}
			}]
		},
		legend: {
				display: false
			},
		tooltips: {
			backgroundColor: '#595959',
			titleMarginBottom: 10
		}
	};
	var data = {
		labels: ['Category 1', 'Category 2', 'Category 3', 'Category 4'],
		datasets: [{
			axis: 'y',
			label: 'My entries',
			data: [category1count, category2count, category3count, category4count],
			backgroundColor: [
				'rgba(230,230,230,0.3)',
				'rgba(230,230,230,0.3)',
				'rgba(230,230,230,0.3)',
				'rgba(230,230,230,0.3)'
			],
			borderColor: [
				'#cccccc',
				'#cccccc',
				'#cccccc',
				'#cccccc'
			],
			hoverOffset: 4,
			borderWidth: 2
		}]
	};


	var myObsChart = new Chart(ctx,{type: 'horizontalBar', data:data, options:options});