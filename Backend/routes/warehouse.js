const express = require("express");
const router = express.Router();
const catchAsync = require('../utils/CatchAsync');
const warehouse = require("../controller/warehouse");



router.route("/createwarehouse")
    .post(catchAsync(warehouse.createWarehouse))

router.route("/getwarehouse/:id")
    .get(catchAsync(warehouse.getWarehouse))

router.route("/getallwarehouses/:id")
    .get(catchAsync(warehouse.getAllWarehouses))
    
    router.route("/getwarehousebyname/:name")
    .get(catchAsync(warehouse.getWarehouseByName));


module.exports = router;