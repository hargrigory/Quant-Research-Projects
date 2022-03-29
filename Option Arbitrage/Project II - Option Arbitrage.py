data_string = """Time,BidPrice-Stock,BidVolume-Stock,AskPrice-Stock,AskVolume-Stock,TimeToExpiry,BidPrice-P60,BidVolume-P60,AskPrice-P60,AskVolume-P60,BidPrice-P70,BidVolume-P70,AskPrice-P70,AskVolume-P70,BidPrice-P80,BidVolume-P80,AskPrice-P80,AskVolume-P80,BidPrice-C60,BidVolume-C60,AskPrice-C60,AskVolume-C60,BidPrice-C70,BidVolume-C70,AskPrice-C70,AskVolume-C70,BidPrice-C80,BidVolume-C80,AskPrice-C80,AskVolume-C80
2018-01-01 00:05:00,70.7,120.0,70.9,120.0,0.911624809741248,1.3,20.0,1.35,20.0,4.92,20.0,5.0200000000000005,20.0,11.42,20.0,11.53,20.0,12.06,20.0,12.17,20.0,5.71,20.0,5.8100000000000005,20.0,2.22,20.0,2.3000000000000003,20.0
2018-01-01 00:10:00,70.75,116.0,71.0,119.0,0.9116152968036529,1.28,20.0,1.33,18.0,4.93,19.0,5.03,21.0,11.39,20.0,11.5,20.0,12.08,20.0,12.19,19.0,5.74,19.0,5.8500000000000005,21.0,2.23,18.0,2.32,20.0
2018-01-01 00:15:00,70.85000000000001,120.0,71.05,107.0,0.9116057838660578,1.28,23.0,1.33,20.0,4.96,18.0,5.07,19.0,11.36,21.0,11.47,22.0,12.11,20.0,12.22,19.0,5.7700000000000005,20.0,5.88,24.0,2.25,19.0,2.34,20.0
2018-01-01 00:20:00,70.8,121.0,71.05,120.0,0.9115962709284626,1.31,22.0,1.36,21.0,5.0,17.0,5.1000000000000005,17.0,11.42,19.0,11.53,22.0,12.11,19.0,12.21,18.0,5.75,22.0,5.87,21.0,2.3000000000000003,18.0,2.39,19.0
2018-01-01 00:25:00,70.75,137.0,71.0,139.0,0.9115867579908675,1.3,24.0,1.35,21.0,5.0,17.0,5.1000000000000005,17.0,11.41,18.0,11.51,20.0,12.11,19.0,12.21,18.0,5.72,22.0,5.84,23.0,2.31,19.0,2.4,19.0
2018-01-01 00:30:00,70.8,133.0,71.0,132.0,0.9115772450532724,1.28,25.0,1.33,23.0,4.96,17.0,5.0600000000000005,17.0,11.36,19.0,11.46,20.0,12.14,22.0,12.24,19.0,5.67,22.0,5.78,23.0,2.2800000000000002,18.0,2.36,17.0
2018-01-01 00:35:00,70.8,132.0,71.05,141.0,0.9115677321156772,1.29,28.0,1.34,21.0,4.94,16.0,5.04,17.0,11.34,22.0,11.450000000000001,24.0,12.11,21.0,12.21,18.0,5.67,21.0,5.79,26.0,2.2,17.0,2.2800000000000002,17.0
2018-01-01 00:40:00,70.75,129.0,71.05,132.0,0.9115582191780821,1.31,24.0,1.37,24.0,4.91,15.0,5.01,18.0,11.38,21.0,11.49,22.0,12.1,22.0,12.200000000000001,21.0,5.73,20.0,5.8500000000000005,24.0,2.2600000000000002,16.0,2.34,16.0
2018-01-01 00:45:00,70.8,143.0,71.05,135.0,0.911548706240487,1.31,24.0,1.36,23.0,4.97,15.0,5.07,20.0,11.39,24.0,11.51,25.0,12.09,20.0,12.200000000000001,20.0,5.69,24.0,5.8100000000000005,25.0,2.29,15.0,2.37,14.0
2018-01-01 00:50:00,70.7,151.0,70.95,134.0,0.9115391933028919,1.31,25.0,1.37,22.0,5.04,15.0,5.14,17.0,11.48,22.0,11.59,26.0,12.01,20.0,12.13,19.0,5.61,21.0,5.74,22.0,2.2,14.0,2.2800000000000002,14.0
2018-01-01 00:55:00,70.65,175.0,70.9,156.0,0.9115296803652968,1.31,24.0,1.37,21.0,5.07,14.0,5.17,15.0,11.51,21.0,11.63,25.0,12.01,22.0,12.13,21.0,5.59,22.0,5.72,23.0,2.22,15.0,2.3000000000000003,14.0
2018-01-01 01:00:00,70.7,148.0,70.95,150.0,0.9115201674277016,1.29,23.0,1.35,20.0,5.01,16.0,5.12,15.0,11.450000000000001,22.0,11.57,22.0,12.09,25.0,12.22,20.0,5.65,20.0,5.78,24.0,2.2,13.0,2.2800000000000002,14.0
2018-01-01 01:05:00,70.7,139.0,70.95,130.0,0.9115106544901065,1.33,23.0,1.3900000000000001,26.0,4.99,16.0,5.09,16.0,11.4,19.0,11.52,19.0,12.08,22.0,12.22,21.0,5.69,22.0,5.83,23.0,2.17,14.0,2.2600000000000002,15.0
2018-01-01 01:10:00,70.75,153.0,71.0,136.0,0.9115011415525114,1.3,22.0,1.37,27.0,4.97,18.0,5.08,21.0,11.38,21.0,11.51,20.0,12.11,20.0,12.24,20.0,5.72,22.0,5.8500000000000005,22.0,2.2,13.0,2.2800000000000002,13.0
2018-01-01 01:15:00,70.8,156.0,71.0,144.0,0.9114916286149162,1.28,19.0,1.35,24.0,4.92,19.0,5.0200000000000005,22.0,11.33,23.0,11.44,22.0,12.13,20.0,12.25,20.0,5.78,22.0,5.91,23.0,2.27,14.0,2.36,13.0
2018-01-01 01:20:00,70.75,142.0,71.0,137.0,0.9114821156773211,1.3,23.0,1.36,24.0,4.96,20.0,5.07,20.0,11.370000000000001,20.0,11.48,25.0,12.05,22.0,12.16,21.0,5.71,27.0,5.83,26.0,2.23,14.0,2.32,13.0
2018-01-01 01:25:00,70.75,144.0,71.0,131.0,0.911472602739726,1.29,23.0,1.36,22.0,4.91,20.0,5.01,21.0,11.33,20.0,11.450000000000001,24.0,12.040000000000001,19.0,12.16,20.0,5.73,26.0,5.8500000000000005,24.0,2.25,14.0,2.35,13.0
2018-01-01 01:30:00,70.65,136.0,70.9,131.0,0.9114630898021309,1.32,24.0,1.3800000000000001,21.0,4.94,23.0,5.04,21.0,11.48,20.0,11.59,24.0,11.97,19.0,12.07,18.0,5.68,25.0,5.79,26.0,2.2600000000000002,14.0,2.34,13.0
2018-01-01 01:35:00,70.65,136.0,70.9,126.0,0.9114535768645358,1.31,23.0,1.37,21.0,4.92,25.0,5.0200000000000005,23.0,11.42,18.0,11.53,23.0,12.030000000000001,18.0,12.13,18.0,5.71,25.0,5.82,24.0,2.25,16.0,2.33,13.0
2018-01-01 01:40:00,70.65,129.0,70.9,124.0,0.9114440639269406,1.33,24.0,1.3800000000000001,23.0,4.99,26.0,5.1000000000000005,23.0,11.450000000000001,17.0,11.56,20.0,12.040000000000001,17.0,12.14,20.0,5.69,22.0,5.79,24.0,2.22,17.0,2.3000000000000003,14.0
2018-01-01 01:45:00,70.60000000000001,125.0,70.8,132.0,0.9114345509893454,1.33,24.0,1.3900000000000001,24.0,5.01,23.0,5.11,24.0,11.5,19.0,11.61,23.0,11.94,17.0,12.040000000000001,18.0,5.63,21.0,5.74,23.0,2.2,19.0,2.29,16.0
2018-01-01 01:50:00,70.60000000000001,119.0,70.8,135.0,0.9114250380517503,1.33,27.0,1.3900000000000001,24.0,5.0200000000000005,23.0,5.12,23.0,11.53,19.0,11.65,22.0,11.93,17.0,12.040000000000001,22.0,5.64,20.0,5.75,22.0,2.19,17.0,2.2800000000000002,17.0
2018-01-01 01:55:00,70.60000000000001,133.0,70.8,117.0,0.9114155251141552,1.33,23.0,1.3900000000000001,23.0,5.0200000000000005,25.0,5.12,19.0,11.56,19.0,11.67,22.0,11.94,16.0,12.040000000000001,19.0,5.64,20.0,5.76,23.0,2.15,21.0,2.24,18.0
2018-01-01 02:00:00,70.5,136.0,70.7,122.0,0.91140601217656,1.33,23.0,1.3800000000000001,24.0,5.05,21.0,5.15,23.0,11.55,17.0,11.67,22.0,11.88,16.0,11.99,18.0,5.63,22.0,5.74,23.0,2.14,21.0,2.23,19.0
2018-01-01 02:05:00,70.5,133.0,70.7,125.0,0.9113964992389649,1.34,25.0,1.4000000000000001,25.0,5.04,22.0,5.14,24.0,11.58,16.0,11.700000000000001,22.0,11.790000000000001,15.0,11.9,19.0,5.59,23.0,5.71,20.0,2.15,20.0,2.25,19.0
2018-01-01 02:10:00,70.5,139.0,70.7,107.0,0.9113869863013698,1.34,23.0,1.4000000000000001,25.0,5.03,21.0,5.13,22.0,11.56,15.0,11.68,20.0,11.86,16.0,11.98,17.0,5.59,20.0,5.72,18.0,2.16,19.0,2.2600000000000002,22.0
2018-01-01 02:15:00,70.45,145.0,70.65,109.0,0.9113774733637747,1.3,21.0,1.36,22.0,4.98,16.0,5.09,20.0,11.59,16.0,11.72,20.0,11.870000000000001,16.0,11.99,17.0,5.57,21.0,5.69,21.0,2.14,20.0,2.24,21.0
2018-01-01 02:20:00,70.45,128.0,70.65,98.0,0.9113679604261795,1.3,19.0,1.36,22.0,5.0,18.0,5.1000000000000005,19.0,11.620000000000001,17.0,11.74,20.0,11.9,17.0,12.02,17.0,5.62,21.0,5.74,24.0,2.13,22.0,2.22,20.0
2018-01-01 02:25:00,70.4,124.0,70.60000000000001,95.0,0.9113584474885844,1.35,19.0,1.41,23.0,5.07,19.0,5.17,23.0,11.72,18.0,11.84,20.0,11.81,18.0,11.92,18.0,5.62,22.0,5.73,21.0,2.09,20.0,2.18,19.0
2018-01-01 02:30:00,70.4,107.0,70.60000000000001,93.0,0.9113489345509893,1.35,20.0,1.41,24.0,5.09,19.0,5.19,21.0,11.73,18.0,11.85,21.0,11.82,18.0,11.94,17.0,5.63,21.0,5.75,23.0,2.09,23.0,2.18,21.0
2018-01-01 02:35:00,70.45,94.0,70.65,86.0,0.9113394216133942,1.36,19.0,1.42,26.0,5.08,17.0,5.18,21.0,11.67,19.0,11.790000000000001,20.0,11.88,16.0,11.99,18.0,5.65,21.0,5.76,21.0,2.13,21.0,2.21,20.0
2018-01-01 02:40:00,70.45,91.0,70.65,89.0,0.911329908675799,1.35,21.0,1.42,24.0,5.05,18.0,5.14,20.0,11.66,20.0,11.78,21.0,11.86,16.0,11.97,16.0,5.6000000000000005,20.0,5.7,17.0,2.1,23.0,2.19,20.0
2018-01-01 02:45:00,70.45,104.0,70.7,83.0,0.9113203957382039,1.32,25.0,1.3900000000000001,27.0,5.01,19.0,5.11,20.0,11.61,21.0,11.73,17.0,11.83,15.0,11.94,14.0,5.64,19.0,5.74,18.0,2.11,23.0,2.2,19.0
2018-01-01 02:50:00,70.45,99.0,70.7,86.0,0.9113108828006088,1.32,26.0,1.3900000000000001,24.0,4.98,20.0,5.07,22.0,11.57,20.0,11.69,17.0,11.83,15.0,11.93,15.0,5.65,18.0,5.75,17.0,2.11,24.0,2.2,19.0
2018-01-01 02:55:00,70.5,91.0,70.7,87.0,0.9113013698630137,1.3,25.0,1.37,24.0,4.95,21.0,5.04,21.0,11.56,20.0,11.68,19.0,11.870000000000001,15.0,11.96,16.0,5.68,16.0,5.78,17.0,2.13,24.0,2.21,19.0
2018-01-01 03:00:00,70.55,89.0,70.75,77.0,0.9112918569254185,1.29,21.0,1.36,21.0,4.93,23.0,5.0200000000000005,23.0,11.58,20.0,11.700000000000001,18.0,11.89,14.0,11.99,16.0,5.64,17.0,5.74,17.0,2.1,22.0,2.18,19.0
2018-01-01 03:05:00,70.55,85.0,70.75,76.0,0.9112823439878234,1.29,20.0,1.36,19.0,4.94,25.0,5.0200000000000005,23.0,11.57,19.0,11.69,16.0,11.91,14.0,12.01,17.0,5.65,17.0,5.75,18.0,2.16,23.0,2.24,20.0
2018-01-01 03:10:00,70.5,87.0,70.75,82.0,0.9112728310502283,1.29,23.0,1.35,19.0,4.92,25.0,5.01,24.0,11.57,19.0,11.69,17.0,11.86,14.0,11.96,17.0,5.69,16.0,5.78,18.0,2.14,21.0,2.22,20.0
2018-01-01 03:15:00,70.5,89.0,70.7,80.0,0.9112633181126332,1.3,23.0,1.36,21.0,4.9,24.0,4.98,24.0,11.57,21.0,11.69,20.0,11.85,15.0,11.950000000000001,16.0,5.67,18.0,5.76,18.0,2.18,22.0,2.25,24.0
2018-01-01 03:20:00,70.5,80.0,70.7,77.0,0.911253805175038,1.32,24.0,1.3800000000000001,21.0,4.92,26.0,5.01,25.0,11.55,22.0,11.67,20.0,11.89,16.0,11.99,16.0,5.69,19.0,5.79,19.0,2.16,21.0,2.24,20.0
2018-01-01 03:25:00,70.35000000000001,82.0,70.60000000000001,82.0,0.9112442922374429,1.35,25.0,1.41,22.0,4.99,27.0,5.07,25.0,11.61,24.0,11.73,20.0,11.81,16.0,11.91,16.0,5.57,20.0,5.67,21.0,2.13,23.0,2.2,21.0
2018-01-01 03:30:00,70.4,92.0,70.60000000000001,83.0,0.9112347792998478,1.36,26.0,1.42,21.0,4.97,26.0,5.0600000000000005,24.0,11.67,23.0,11.790000000000001,19.0,11.8,15.0,11.9,16.0,5.6000000000000005,19.0,5.7,21.0,2.12,24.0,2.19,22.0
2018-01-01 03:35:00,70.45,102.0,70.65,90.0,0.9112252663622527,1.34,23.0,1.3900000000000001,20.0,5.0200000000000005,24.0,5.09,25.0,11.620000000000001,22.0,11.73,20.0,11.85,16.0,11.950000000000001,15.0,5.58,21.0,5.68,22.0,2.14,24.0,2.21,20.0
2018-01-01 03:40:00,70.5,109.0,70.7,92.0,0.9112157534246574,1.33,22.0,1.3800000000000001,20.0,4.98,24.0,5.0600000000000005,23.0,11.57,22.0,11.68,19.0,11.94,16.0,12.040000000000001,15.0,5.64,21.0,5.73,22.0,2.18,22.0,2.25,19.0
2018-01-01 03:45:00,70.4,108.0,70.60000000000001,88.0,0.9112062404870623,1.33,23.0,1.3900000000000001,20.0,5.03,20.0,5.11,23.0,11.56,21.0,11.67,18.0,11.93,15.0,12.030000000000001,17.0,5.59,21.0,5.69,24.0,2.14,19.0,2.22,19.0
2018-01-01 03:50:00,70.4,115.0,70.60000000000001,93.0,0.9111967275494672,1.37,23.0,1.43,19.0,5.09,19.0,5.18,24.0,11.620000000000001,20.0,11.73,17.0,11.89,17.0,11.99,17.0,5.51,20.0,5.61,22.0,2.08,20.0,2.16,21.0
2018-01-01 03:55:00,70.4,101.0,70.60000000000001,100.0,0.9111872146118721,1.3800000000000001,24.0,1.45,20.0,5.01,21.0,5.09,22.0,11.58,20.0,11.68,18.0,11.89,17.0,11.99,15.0,5.45,22.0,5.55,24.0,2.13,20.0,2.21,21.0
2018-01-01 04:00:00,70.4,104.0,70.60000000000001,124.0,0.9111777016742769,1.3900000000000001,23.0,1.45,19.0,5.0200000000000005,20.0,5.1000000000000005,20.0,11.61,20.0,11.71,19.0,11.83,17.0,11.93,18.0,5.48,20.0,5.57,23.0,2.09,18.0,2.18,22.0
2018-01-01 04:05:00,70.45,105.0,70.60000000000001,138.0,0.9111681887366818,1.3800000000000001,22.0,1.44,16.0,5.0600000000000005,20.0,5.13,21.0,11.61,18.0,11.71,18.0,11.85,17.0,11.950000000000001,19.0,5.47,22.0,5.5600000000000005,23.0,2.14,18.0,2.22,23.0
2018-01-01 04:10:00,70.35000000000001,108.0,70.55,125.0,0.9111586757990867,1.37,20.0,1.42,15.0,5.1000000000000005,19.0,5.18,22.0,11.700000000000001,18.0,11.8,17.0,11.82,16.0,11.92,19.0,5.46,21.0,5.54,23.0,2.18,18.0,2.27,21.0
2018-01-01 04:15:00,70.4,104.0,70.60000000000001,119.0,0.9111491628614916,1.32,22.0,1.37,17.0,5.05,20.0,5.13,22.0,11.63,17.0,11.73,20.0,11.85,15.0,11.96,18.0,5.5,23.0,5.59,23.0,2.2,19.0,2.29,23.0
2018-01-01 04:20:00,70.45,103.0,70.7,127.0,0.9111396499238964,1.35,21.0,1.4000000000000001,20.0,5.0200000000000005,20.0,5.11,19.0,11.63,18.0,11.74,18.0,11.86,16.0,11.97,19.0,5.5,22.0,5.61,24.0,2.16,19.0,2.25,25.0
2018-01-01 04:25:00,70.55,96.0,70.8,101.0,0.9111301369863013,1.32,21.0,1.3800000000000001,20.0,5.04,21.0,5.13,21.0,11.540000000000001,17.0,11.65,18.0,11.93,17.0,12.05,19.0,5.5600000000000005,23.0,5.66,22.0,2.17,21.0,2.2600000000000002,25.0
2018-01-01 04:30:00,70.5,96.0,70.7,98.0,0.9111206240487062,1.32,21.0,1.3800000000000001,23.0,5.05,23.0,5.14,19.0,11.620000000000001,18.0,11.73,16.0,11.89,19.0,12.0,21.0,5.59,24.0,5.69,25.0,2.16,21.0,2.25,26.0
2018-01-01 04:35:00,70.55,90.0,70.8,90.0,0.9111111111111111,1.3,21.0,1.35,25.0,4.99,22.0,5.09,19.0,11.56,17.0,11.67,17.0,11.93,19.0,12.040000000000001,19.0,5.63,26.0,5.74,22.0,2.19,19.0,2.2800000000000002,27.0
2018-01-01 04:40:00,70.60000000000001,94.0,70.85000000000001,77.0,0.9111015981735159,1.29,21.0,1.34,23.0,4.99,19.0,5.08,19.0,11.56,17.0,11.66,18.0,11.96,18.0,12.06,17.0,5.63,24.0,5.73,19.0,2.2,19.0,2.29,26.0
2018-01-01 04:45:00,70.60000000000001,85.0,70.8,79.0,0.9110920852359208,1.32,24.0,1.37,23.0,4.95,17.0,5.03,17.0,11.52,20.0,11.620000000000001,19.0,11.99,18.0,12.1,16.0,5.64,25.0,5.75,22.0,2.18,19.0,2.27,27.0
2018-01-01 04:50:00,70.60000000000001,95.0,70.8,93.0,0.9110825722983257,1.33,24.0,1.3800000000000001,24.0,4.97,15.0,5.0600000000000005,17.0,11.56,21.0,11.66,19.0,12.0,17.0,12.11,17.0,5.68,23.0,5.78,24.0,2.19,18.0,2.2800000000000002,24.0
2018-01-01 04:55:00,70.55,92.0,70.75,85.0,0.9110730593607306,1.34,23.0,1.3900000000000001,21.0,5.05,17.0,5.14,16.0,11.64,20.0,11.75,18.0,11.93,16.0,12.040000000000001,18.0,5.62,25.0,5.73,23.0,2.16,18.0,2.25,23.0
2018-01-01 05:00:00,70.55,99.0,70.75,88.0,0.9110635464231354,1.31,22.0,1.36,22.0,5.05,18.0,5.13,16.0,11.63,20.0,11.73,16.0,11.94,16.0,12.05,16.0,5.67,23.0,5.7700000000000005,22.0,2.14,19.0,2.22,22.0
2018-01-01 05:05:00,70.5,93.0,70.75,86.0,0.9110540334855403,1.31,22.0,1.36,23.0,5.03,19.0,5.12,17.0,11.63,21.0,11.73,15.0,11.93,16.0,12.040000000000001,15.0,5.62,24.0,5.71,22.0,2.15,20.0,2.24,24.0
2018-01-01 05:10:00,70.5,98.0,70.7,82.0,0.9110445205479452,1.34,23.0,1.4000000000000001,22.0,5.04,19.0,5.12,16.0,11.6,18.0,11.71,16.0,11.9,15.0,12.01,18.0,5.55,22.0,5.66,21.0,2.16,20.0,2.2600000000000002,23.0
2018-01-01 05:15:00,70.5,97.0,70.7,74.0,0.9110350076103501,1.34,22.0,1.3900000000000001,21.0,4.99,21.0,5.08,17.0,11.620000000000001,17.0,11.72,16.0,11.870000000000001,17.0,11.98,21.0,5.53,22.0,5.64,22.0,2.15,21.0,2.24,23.0
2018-01-01 05:20:00,70.5,97.0,70.75,85.0,0.9110254946727548,1.34,22.0,1.3900000000000001,20.0,5.03,23.0,5.12,17.0,11.56,19.0,11.67,17.0,11.91,18.0,12.02,21.0,5.59,21.0,5.71,21.0,2.14,20.0,2.24,22.0
2018-01-01 05:25:00,70.45,106.0,70.7,84.0,0.9110159817351597,1.32,21.0,1.37,20.0,5.04,21.0,5.13,15.0,11.6,18.0,11.71,21.0,11.86,18.0,11.98,20.0,5.57,20.0,5.69,23.0,2.13,21.0,2.22,24.0
2018-01-01 05:30:00,70.55,97.0,70.8,85.0,0.9110064687975646,1.28,25.0,1.34,22.0,4.97,22.0,5.07,15.0,11.49,18.0,11.6,22.0,11.97,16.0,12.09,18.0,5.64,21.0,5.75,22.0,2.18,20.0,2.27,22.0
2018-01-01 05:35:00,70.5,86.0,70.7,82.0,0.9109969558599695,1.29,22.0,1.35,21.0,4.96,21.0,5.0600000000000005,14.0,11.52,18.0,11.63,22.0,11.93,17.0,12.05,17.0,5.61,20.0,5.71,24.0,2.19,21.0,2.29,21.0
2018-01-01 05:40:00,70.45,87.0,70.7,87.0,0.9109874429223743,1.28,21.0,1.33,22.0,4.95,19.0,5.04,15.0,11.53,20.0,11.64,19.0,11.9,20.0,12.030000000000001,17.0,5.59,20.0,5.69,21.0,2.12,18.0,2.22,19.0
2018-01-01 05:45:00,70.5,90.0,70.75,86.0,0.9109779299847792,1.29,23.0,1.34,22.0,4.96,18.0,5.05,15.0,11.46,20.0,11.58,20.0,11.97,20.0,12.1,19.0,5.65,21.0,5.75,19.0,2.17,17.0,2.2600000000000002,18.0
2018-01-01 05:50:00,70.55,88.0,70.75,83.0,0.9109684170471841,1.27,31.0,1.33,23.0,4.96,18.0,5.0600000000000005,16.0,11.46,20.0,11.57,18.0,11.97,20.0,12.09,18.0,5.66,23.0,5.76,19.0,2.19,20.0,2.2800000000000002,21.0
2018-01-01 05:55:00,70.55,88.0,70.75,84.0,0.910958904109589,1.29,28.0,1.35,23.0,4.94,17.0,5.03,16.0,11.44,18.0,11.55,20.0,11.99,19.0,12.11,18.0,5.67,24.0,5.7700000000000005,19.0,2.22,24.0,2.32,20.0
2018-01-01 06:00:00,70.65,91.0,70.85000000000001,91.0,0.9109493911719938,1.26,28.0,1.32,28.0,4.94,16.0,5.03,17.0,11.370000000000001,20.0,11.47,21.0,12.07,20.0,12.18,19.0,5.68,24.0,5.7700000000000005,20.0,2.2600000000000002,26.0,2.35,19.0
2018-01-01 06:05:00,70.65,82.0,70.85000000000001,85.0,0.9109398782343987,1.26,29.0,1.31,29.0,4.9,14.0,5.0,16.0,11.370000000000001,21.0,11.48,20.0,12.08,20.0,12.19,21.0,5.67,24.0,5.7700000000000005,20.0,2.25,23.0,2.36,20.0
2018-01-01 06:10:00,70.7,79.0,70.9,73.0,0.9109303652968036,1.27,30.0,1.32,29.0,4.92,14.0,5.01,15.0,11.41,20.0,11.52,21.0,12.07,20.0,12.17,20.0,5.67,20.0,5.76,18.0,2.27,25.0,2.37,21.0
2018-01-01 06:15:00,70.7,92.0,70.95,79.0,0.9109208523592085,1.23,29.0,1.29,27.0,4.89,15.0,4.98,16.0,11.42,21.0,11.53,21.0,12.040000000000001,18.0,12.15,20.0,5.66,18.0,5.76,18.0,2.27,23.0,2.36,20.0
2018-01-01 06:20:00,70.75,87.0,70.95,85.0,0.9109113394216133,1.24,29.0,1.29,26.0,4.84,15.0,4.93,16.0,11.370000000000001,22.0,11.47,20.0,12.08,17.0,12.18,22.0,5.69,15.0,5.79,18.0,2.2800000000000002,23.0,2.37,22.0
2018-01-01
"""

from scipy import stats
import numpy as np
_norm_cdf = stats.norm(0, 1).cdf
_norm_pdf = stats.norm(0, 1).pdf
def _d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def _d2(S, K, T, r, sigma):
    return _d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def call_value(S, K, T, r, sigma):
    return S * _norm_cdf(_d1(S, K, T, r, sigma)) - K * np.exp(-r * T) * _norm_cdf(_d2(S, K, T, r, sigma))

def put_value(S, K, T, r, sigma):
    return np.exp(-r * T) * K * _norm_cdf(-_d2(S, K, T, r, sigma)) - S * _norm_cdf(-_d1(S, K, T, r, sigma))

def call_delta(S, K, T, r, sigma):
       return _norm_cdf(_d1(S, K, T, r, sigma))

def put_delta(S, K, T, r, sigma):
       return call_delta(S, K, T, r, sigma) - 1

def call_vega(S, K, T, r, sigma):
    return S * _norm_pdf(_d1(S, K, T, r, sigma)) * np.sqrt(T)

def put_vega(S, K, T, r, sigma):
    return call_vega(S, K, T, r, sigma)


import io
import unittest



import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from black_scholes import call_value, put_value, call_delta, put_delta, call_vega, put_vega

def read_data(filename):
    # use the panda library to read the csv file reprsented by the variable filename
    # you will specify that the first column is the index by using index_col=0
    # you will create a variable to store TimeToExpiry series
    # you will create a variable to store the stock series
    # you will create a variable to store all the options Put and Call
    # you will create a dataframe market_data to store stock and options
    # you will return the TimeToExpiry variable and the market_data variable
    df = pd.read_csv(filename, index_col=0)
    # print(df.columns)
    time_to_expiry = df.filter(like='TimeToExpiry')

    stock = df.filter(like='Stock')
    stock.columns = [stock.columns.str[-5:], stock.columns.str[:-6]]
    
    options = pd.concat((df.filter(like='-P'), df.filter(like='-C')), axis=1)
    # options = pd.concat((df[['-P']], df[['-C']]), axis=1)
    options.columns = [options.columns.str[-3:], options.columns.str[:-4]]
    
    market_data = pd.concat((stock, options), axis=1)
    
    return time_to_expiry, market_data


def get_list_of_all_instruments(market_data):
    # Get the variable option names to return all the names of the options
    instruments_names = list(market_data.columns.get_level_values(0).unique())
    option_names = instruments_names[1:]

    return option_names


def set_tte_to_market_data(market_data, time_to_expiry):
    # Add time_to_expiry to market_data
    market_data['TTE'] = time_to_expiry['TimeToExpiry']
    timestamp = market_data.index
    market_data = market_data.set_index('TTE')
    
    return market_data


def create_df_to_store_options_values_delta(market_data, option_names):
    # Create Empty Dictionaries
    # for: 
    short_call_values = {}
    long_call_values = {}
    long_put_values = {}
    short_put_values = {}
    short_call_deltas = {}
    long_call_deltas = {}
    long_put_deltas = {}
    short_put_deltas = {}
    option_values = {}
    option_deltas = {}

    # Set known attributes
    r = 0
    sigma = 0.20
    
    # Forloop to create new columns with Call/Put names
    for option in option_names:
        # Retrieve K from the Option
        K = int(option[-2:])

        if 'C' in option:
            short_call_values[option] = []
            long_call_values[option] = []
            short_call_deltas[option] = []
            long_call_deltas[option] = []

            # Forloop to calculate short/long call values and deltas
            for time, stock_value in market_data.iterrows():
                short_call_values[option].append(call_value(
                    stock_value['Stock', 'AskPrice'], K, time, r, sigma))
                long_call_values[option].append(call_value(
                    stock_value['Stock', 'BidPrice'], K, time, r, sigma))
                long_call_deltas[option].append(call_delta(
                    stock_value['Stock', 'BidPrice'], K, time, r, sigma))
                short_call_deltas[option].append(-call_delta(
                    stock_value['Stock', 'AskPrice'], K, time, r, sigma))

            option_values['Short Call', option] = short_call_values[option]
            option_values['Long Call', option] = long_call_values[option]
            option_deltas['Short Call', option] = short_call_deltas[option]
            option_deltas['Long Call', option] = long_call_deltas[option]

        if 'P' in option:
            long_put_values[option] = []
            short_put_values[option] = []
            long_put_deltas[option] = []
            short_put_deltas[option] = []

            # Forloop to calculate short/long put values and deltas
            for time, stock_value in market_data.iterrows():
                long_put_values[option].append(
                    put_value(stock_value['Stock', 'AskPrice'], K, time, r, sigma))
                short_put_values[option].append(
                    put_value(stock_value['Stock', 'BidPrice'], K, time, r, sigma))
                long_put_deltas[option].append(
                    put_delta(stock_value['Stock', 'AskPrice'], K, time, r, sigma))
                short_put_deltas[option].append(-put_delta(
                    stock_value['Stock', 'BidPrice'], K, time, r, sigma))

            option_values['Long Put', option] = long_put_values[option]
            option_values['Short Put', option] = short_put_values[option]
            option_deltas['Long Put', option] = long_put_deltas[option]
            option_deltas['Short Put', option] = short_put_deltas[option]

    # Create DataFrames with index market_data
    option_values = pd.DataFrame(option_values, index=market_data.index)
    option_deltas = pd.DataFrame(option_deltas, index=market_data.index)

    # Sort the DataFrames
    option_values = option_values.reindex(sorted(option_values.columns), axis=1)
    option_deltas = option_deltas.reindex(sorted(option_deltas.columns), axis=1)

    # Rounding
    option_values = round(option_values, 2)

    return option_values,option_deltas


def add_blacksholes_data_to_market_data(market_data, option_names,\
                                        option_values,option_deltas):


    # Create Columns for Black Scholes Value in the Data Set
    # This is used for later calculations (algorithm and such)

    for option in option_names:
        
        if 'C' in option:
            market_data[option,
                        'Expected AskPrice'] = option_values['Short Call', option]
            market_data[option,
                        'Expected BidPrice'] = option_values['Long Call', option]
            market_data[option,
                        'Delta Short'] = option_deltas['Short Call', option].values
            market_data[option,
                        'Delta Long'] = option_deltas['Long Call', option].values

        # elif you will do the same for Put
        elif 'P' in option:
            market_data[option,
                        'Expected AskPrice'] = option_values['Short Put', option]
            market_data[option,
                        'Expected BidPrice'] = option_values['Long Put', option]
            market_data[option,
                        'Delta Short'] = option_deltas['Short Put', option].values
            market_data[option,
                        'Delta Long'] = option_deltas['Long Put', option].values

    # Sort Columns
    market_data = market_data.reindex(sorted(market_data.columns), axis=1)

    return market_data

def option_opportunities(option,market_data):
    '''
    This function gives arbitrage opportunities based on whether the price
    of the option is too high or too low.
    '''
    # Call
    if 'C' in option:
        expected1 = market_data[option][(market_data[option, 'BidPrice'] -\
            market_data[option,'Expected AskPrice']) >= 0.10].drop('Expected BidPrice', axis=1)
        expected2 = market_data[option][(market_data[option, 'Expected BidPrice'] -\
            market_data[option, 'AskPrice']) >= 0.10].drop('Expected AskPrice', axis=1)
    
    # Put
    elif 'P' in option:
        expected1 = market_data[option][(market_data[option, 'BidPrice'] -\
            market_data[option,'Expected AskPrice']) >= 0.10].drop('Expected BidPrice', axis=1)
        expected2 = market_data[option][(market_data[option, 'Expected BidPrice'] -\
            market_data[option, 'AskPrice']) >= 0.10].drop('Expected AskPrice', axis=1)

    return expected1, expected2


def create_positions(market_data, option_names, timestamp):
    # Create a Dictionary with Timestamp and Time to Expiry
    # Index of market_data was changed earlier to time to expiry
    trades = {('Timestamp', ''): timestamp,
              ('Time to Expiry', ''): market_data.index}

    # Forloop that adds columns for the Call/Put Positions and Deltas
    # Global function is a changing variable name based on the option
    # For option C60 it will create a variable named positions_call_C60
    for option in option_names:
        if 'C' in option:
            trades['Call Position', option] = []
            trades['Call Delta', option] = []
            globals()['positions_call_' + option] = 0
            
        if 'P' in option:
            trades['Put Position', option] = []
            trades['Put Delta', option] = []
            globals()['positions_put_' + option] = 0
    
    # Forloop over the rows of market_data
    for time, data in market_data.iterrows():
        max_delta = min(data['Stock', 'AskVolume'], data['Stock', 'BidVolume'])

        # Forloop over the option_names with conditions
        for option in option_names:
            
            # if-statements if Call or Put + if Short/Long in Call or Put
            if 'C' in option:
                # Short Call
                if (data[option, 'BidPrice'] - data[option, 'Expected AskPrice']) >= 0.10:
                    short_call_volume = data[option, 'BidVolume']
                    long_call_volume = 0
                
                # Long Call
                elif (data[option, 'Expected BidPrice'] - data[option, 'AskPrice']) >= 0.10:
                    long_call_volume = data[option, 'AskVolume']
                    short_call_volume = 0
                    
                else:
                    long_call_volume = 0
                    short_call_volume = 0
                
                call_trade = long_call_volume - short_call_volume
                
                # Define variable, as set earlier. Note the first position is set to zero
                # otherwise
                # One would get an error here since the variable is then not yet defined.
                globals()['positions_call_' + option] = globals()['positions_call_' + option] +\
                                                            call_trade 
                
                # Add Positions (cumulative)
                trades['Call Position', option].append(globals()['positions_call_' + option])
                
                if globals()['positions_call_' + option] >= 0:
                    long_call_delta = data[option, 'Delta Long']
                    short_call_delta = 0
                    
                elif globals()['positions_call_' + option] < 0:
                    short_call_delta = data[option, 'Delta Short']
                    long_call_delta = 0
                
                # Add Deltas (cumulative)
                trades['Call Delta', option].append(
                    abs(globals()['positions_call_' + option]) *\
                        (long_call_delta + short_call_delta))
            
            # if-statement if Call or Put + if Short/Long in Call or Put
            if 'P' in option:        
                # Short Put
                if (data[option, 'BidPrice'] - data[option, 'Expected AskPrice']) >= 0.10:
                    short_put_volume = data[option, 'BidVolume']
                    long_put_volume = 0
                    
                # Long Put
                elif (data[option, 'Expected BidPrice'] - data[option, 'AskPrice']) >= 0.10:
                    long_put_volume = data[option, 'AskVolume']
                    short_put_volume = 0
                
                else:
                    long_put_volume = 0
                    short_put_volume = 0
                    
                put_trade = long_put_volume - short_put_volume
                # Define variable, as set earlier. Note the first position is set to zero
                # otherwise
                # One would get an error here since the variable is then not yet defined.
                globals()['positions_put_' + option] = globals()['positions_put_' + option] +\
                                                            put_trade 
                
                # Add Positions (cumulative)
                trades['Put Position', option].append(globals()['positions_put_' + option])
                
                if globals()['positions_put_' + option] >= 0:
                    long_put_delta = data[option, 'Delta Long']
                    short_put_delta = 0
                    
                elif globals()['positions_put_' + option] < 0:
                    short_put_delta = data[option, 'Delta Short']
                    long_put_delta = 0
                
                # Add Deltas (cumulative)
                trades['Put Delta', option].append(
                    abs(globals()['positions_put_' + option]) *\
                        (long_put_delta + short_put_delta))
                
    # Create DataFrame with Index Timestamp
    trades = pd.DataFrame(trades).set_index('Timestamp')
    
    # Sort Columns
    trades = trades.reindex(sorted(trades.columns), axis=1)
    
    # Calculate Total Option Delta (based on sorted columns)
    trades['Total Option Delta', ''] = np.sum(trades['Call Delta'], axis=1) +\
                                        np.sum(trades['Put Delta'], axis=1)
    
    # Calculate Cumulative Stock Position (floored if positive, ceiled if negative)
    trades['Stock Position', 'Stock'] = -np.where(trades['Total Option Delta',''] >= 0, 
    np.floor(trades['Total Option Delta','']), np.ceil(trades['Total Option Delta','']))
    
    # Calculate remaining option delta (that remains unhedged)
    # This delta is included in the Total Option Delta again which ensures
    # It always remains below zero
    trades['Remaining Option Delta',''] = trades['Total Option Delta',''] +\
                                            trades['Stock Position', 'Stock']
    # Show DataFrame
    # print(trades.tail())
    
    return trades


def create_orders(positions):
    # Create trades_diff dataframe that gives all actual trades (not positions)
    trades_diff = positions.diff()[1:].drop(['Call Delta', 'Put Delta', 'Time to Expiry',
    'Total Option Delta', 'Remaining Option Delta'], axis=1)
    trades_diff.columns = trades_diff.columns.droplevel(level=0)
    
    final_positions = positions[-1:].drop(['Call Delta', 'Put Delta', 'Time to Expiry',
    'Total Option Delta', 'Remaining Option Delta'], axis=1)
    final_positions.columns = final_positions.columns.droplevel(level=0)
    
    return trades_diff,final_positions
    
class TestArbitrageOption(unittest.TestCase):

    def setUp(self):
        pass

    def test_read_data(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        print("Time to expiry")
        print(time_to_expiry.head(4).to_string())
        print("Market Data")
        print(market_data.head(4).to_string())

    def test_option_names(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        print(get_list_of_all_instruments(market_data))

    def test_option_names(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        set_tte_to_market_data(market_data, time_to_expiry)
        print(market_data.head().to_string())

    def test_create_df_for_option_values_delta(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        option_names = get_list_of_all_instruments(market_data)
        market_data = set_tte_to_market_data(market_data, time_to_expiry)
        option_values, option_deltas = \
            create_df_to_store_options_values_delta(market_data, \
                                                    option_names)
        # Show DataFrames
        print('Option Values')
        print(option_values.head().to_string())
        print('Option Deltas')
        print(option_deltas.head().to_string())

    def test_add_blacksholes_data_to_market_data(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        option_names = get_list_of_all_instruments(market_data)
        market_data = set_tte_to_market_data(market_data, time_to_expiry)
        option_values, option_deltas = \
            create_df_to_store_options_values_delta(market_data, \
                                                    option_names)
        df = add_blacksholes_data_to_market_data(market_data, \
                                                 option_names,\
                                                 option_values,\
                                                 option_deltas)
        print(df.head(10).to_string())


    def test_option_opportunity(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        option_names = get_list_of_all_instruments(market_data)
        market_data = set_tte_to_market_data(market_data, time_to_expiry)
        option_values, option_deltas = \
            create_df_to_store_options_values_delta(market_data, \
                                                    option_names)
        market_data = add_blacksholes_data_to_market_data(market_data, \
                                                 option_names,\
                                                 option_values,\
                                                 option_deltas)
        option="C80"
        oo=option_opportunities(option,market_data)
        print('BidPrice is at least 0.10 higher than Expected AskPrice for Option ' + option)
        print(oo[0].head().to_string())
        print('AskPrice is at least 0.10 lower than Expected BidPrice for Option ' + option)
        print(oo[1].head().to_string())
        print('The amount of trades are', len(oo[0]) + len(oo[1]))

    def test_create_positions(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        timestamp = market_data.index
        option_names = get_list_of_all_instruments(market_data)
        market_data = set_tte_to_market_data(market_data, time_to_expiry)
        option_values, option_deltas = \
            create_df_to_store_options_values_delta(market_data, \
                                                    option_names)
        market_data = add_blacksholes_data_to_market_data(market_data, \
                                                 option_names,\
                                                 option_values,\
                                                 option_deltas)
        positions=create_positions(market_data,option_names,timestamp)
        print(positions.tail().to_string())

    def test_create_orders(self):
        filename = io.StringIO(data_string)
        time_to_expiry, market_data = read_data(filename)
        timestamp = market_data.index
        option_names = get_list_of_all_instruments(market_data)
        market_data = set_tte_to_market_data(market_data, time_to_expiry)
        option_values, option_deltas = \
            create_df_to_store_options_values_delta(market_data, \
                                                    option_names)
        market_data = add_blacksholes_data_to_market_data(market_data, \
                                                 option_names,\
                                                 option_values,\
                                                 option_deltas)
        positions=create_positions(market_data,option_names,timestamp)
        order,final_position=create_orders(positions)
        print("Orders")
        print(order.tail(5).to_string())
        print("Final position")
        print(final_position)



if __name__ == '__main__':
    tao = TestArbitrageOption()
    tao.setUp()
    func_name = input().strip()
    tao.__getattribute__(func_name)()
