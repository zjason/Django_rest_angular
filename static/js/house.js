(function() {
  var app = angular.module('house',[]);

  app.controller('HouseController', function($scope, $http){
    $scope.initFirst=function(){
      $http.get('http://127.0.0.1:8000/house').success(function(data){
        $scope.test = data;
      });
    };
    // $http.get('http://127.0.0.1:8000/house').success(function(data){
    //   $scope.test = data;
    // });

    $scope.SendData = function(){
      var dataobj = {location:$scope.location, desc:$scope.desc, price:$scope.price, hasimage: false};

      $http.post('http://127.0.0.1:8000/house/',dataobj).success(function(data,status){
        $scope.PostDataResponse = data;
        $scope.initFirst();
      }).error(function(data,status){
        $scope.ResponseDetails = "Data: " + data + " status: " + status;
      });
    };

    $scope.Remove = function(id){
      $http.delete('http://127.0.0.1:8000/house/'+id).success(function(data,status){
        $scope.PostDataResponse = data;
        $scope.initFirst();
      }).error(function(data,status){
        $scope.ResponseDetails = "Data: " + data + " status: " + status;
      });
    };

    $scope.Detail = function(id){
      $http.get('http://127.0.0.1:8000/house/'+id).success(function(data){
        $scope.test_detail = data;
      });
    };

    $scope.PriceQ = function(condition){
      $http.get('http://127.0.0.1:8000/house/query/'+condition).success(function(data,status){
        $scope.test = data;
        $scope.PostDataResponse = data;
      }).error(function(data,status){
        $scope.ResponseDetails = "Data: " + data + " status: " + status;
      });
    };

  });
})();
