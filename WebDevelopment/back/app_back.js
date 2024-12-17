/* Import modules แต่ละส่วน */
const express = require('express');
const dotenv = require('dotenv');
const mysql = require('mysql2');
const cors = require('cors');
const path = require("path");

const app = express();

/* เชื่อม environmental variables ที่ระบุไว้ใน .env */
dotenv.config();

/* สร้าง Router object และ register the router */
const router = express.Router();
app.use(router);

router.use(express.json());
router.use(express.urlencoded({ extended: true }));

const corsOptions = {
    origin: "http://localhost:3030", // Allow this origin
    credentials: true,              // Allow credentials
};

router.use(cors(corsOptions));

/* สร้างตัวแปร Connection สำหรับ MySQL ตามข้อมูลในไฟล์ .env */
var Connection = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME
});

/* เชื่อมต่อ Connect ไปที่ฐานข้อมูล */
Connection.connect(function (err) {
    if (err) throw err;
    console.log(`Connected DB: ${process.env.DB_NAME}`);
})

/* ==================== APIs ======================= */

// Testing Select ALL Products
// method: GET
// URL: http://localhost:3031/api/products
router.get('/api/products', cors(), function (req, res) {
    Connection.query('SELECT * FROM Product', function (error, results) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'Products retrieved.' });
    });
});

// Testing Insert a new Product
// method: POST
// URL: http://localhost:3031/api/product
// body: raw JSON
// CASE 1
// {
//  "Product": {
//      "ProductID": 11486822,
//      "PName": "Banana Muffin",
//      "Price": 22,
//      "Description": "Banana muffin, 1 pcs",
//      "Picture": "https://s3.ap-southeast-1.amazonaws.com/lbx-snp-cms/images/menu/6210-wEmStPgcjF1723093577.webp",
//      "Status": 0,
//      "CategoryCode": "C"
//      }
// }
// CASE 2
// {
//  "Product": {
//      "ProductID": 9992700,
//      "PName": "Tuna Sandwich",
//      "Price": 65,
//      "Description": "Tuna sandwich",
//      "Picture": "https://s3.ap-southeast-1.amazonaws.com/lbx-snp-cms/images/menu/3570-PodGV1cPPA1723093560.webp",
//      "Status": 1,
//      "CategoryCode": "S"
//      }
// }
router.post('/api/product', async function (req, res) {
    let product = req.body.Product;
    console.log(req.body)
    console.log(product);
    if (!product) {
        return res.status(400).send({ error: true, message: 'Please provide product information' });
    }
    Connection.query("INSERT INTO Product SET ? ", product, function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
        return res.send({ error: false, data: results.affectedRows, message: 'New product has been added successfully.' });
    });
});

// Testing Insert new Tags
// method: POST
// URL: http://localhost:3031/api/tag
// body: raw JSON
// CASE 1
// {
//  "Tags": {
//      "ProductID": 11486822,
//      "Tag": "Healthy"
//      }
// }
// CASE 2
// {
//  "Tags": {
//      "ProductID": 11486822,
//      "Tag": "Halal"
//      }
// }
router.post('/api/tag', function (req, res) {
    let tag = req.body.Tags;
    console.log(tag);
    if (!tag) {
        return res.status(400).send({ error: true, message: 'Please provide product\'s tag information' });
    }
    Connection.query("INSERT INTO Tags SET ? ", tag, function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
        return res.send({ error: false, data: results.affectedRows, message: 'New Tag\'s tags has been added successfully.' });
    });
});

// Testing Update Product
// method: PUT
// URL: http://localhost:3031/api/product
// body: raw JSON
// CASE 1
// {
//  "Product": {
//      "ProductID": 11486822,
//      "PName": "Banana Cupcake",
//      "Price": 22,
//      "Description": "Banana cupcake, 1 pc",
//      "Picture": "https://s3.ap-southeast-1.amazonaws.com/lbx-snp-cms/images/menu/6210-wEmStPgcjF1723093577.webp",
//      "Status": 1,
//      "CategoryCode": "C"
//      }
// }
// CASE 2
// {
//  "Product": {
//      "ProductID": 9992700,
//      "PName": "Tuna Sandwich",
//      "Price": 65,
//      "Description": "Tuna sandwich, 2 pcs",
//      "Picture": "https://s3.ap-southeast-1.amazonaws.com/lbx-snp-cms/images/menu/3570-PodGV1cPPA1723093560.webp",
//      "Status": 0,
//      "CategoryCode": "B"
//      }
// }
router.put('/api/product', function (req, res) {
    let product_id = req.body.Product.ProductID;
    let product = req.body.Product;
    if (!product_id || !product) {
        return res.status(400).send({ error: product, message: 'Please provide product information' });
    }
    Connection.query("UPDATE Product SET ? WHERE ProductID = ?", [product, product_id], function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
        return res.send({ error: false, data: results.affectedRows, message: 'Product has been updated successfully.' })
    });
});

// Testing Update new Tags
// method: PUT
// URL: http://localhost:3031/api/tag
// body: raw JSON
// CASE 1
// {
//  "Tags": {
//      "ProductID": 11486822,
//      "Tag": "Halal"
//      }
// }
// CASE 2
// {
//  "Tags": {
//      "ProductID": 9992700,
//      "Tag": "Dairy free"
//      }
// }
router.put('/api/tag', function (req, res) {
    let product_id = req.body.Tags.ProductID;
    let product = req.body.Tags;
    if (!product_id || !product) {
        return res.status(400).send({ error: product, message: 'Please provide product\'s tag information' });
    }
    Connection.query("UPDATE Tags SET ? WHERE ProductID = ?", [product, product_id], function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
        return res.send({ error: false, data: results.affectedRows, message: 'Product\'s tag has been updated successfully.' })
    });
});

// Testing Delete Tags and Productby Product ID
// method: DELETE
// URL: http://localhost:3031/api/product
// body: raw JSON
// {
//  "Product": {
//      "ProductID": 11486822
//      }
// }
// {
//  "Product": {
//      "ProductID": 9992700
//      }
// }
router.delete('/api/product', cors(), function (req, res) {
    let product_id = req.body.Product.ProductID;
    if (!product_id) {
        return res.status(400).send({ error: true, message: 'Please provide Product ID' });
    }

    Connection.query('DELETE FROM Tags WHERE ProductID = ?', [product_id], function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
    });

    Connection.query('DELETE FROM Product WHERE ProductID = ?', [product_id], function (error, results) {
        if (error) throw error;
        logAlter(req.url, req.method, req.body);
        return res.send({ error: false, data: results.affectedRows, message: 'Product has been deleted successfully.' });
    });
});

// Testing Select Products by ProductID
// method: GET
// CASE 1
// URL: http://localhost:3031/api/product/11532746
// CASE 2
// URL: http://localhost:3031/api/product/10321778
router.get('/api/product/:id', cors(), function (req, res) {
    let product_id = req.params.id;
    if (!product_id) {
        return res.status(400).send({ error: true, message: 'Please provide product id.' });
    }
    Connection.query('SELECT * FROM Product LEFT JOIN Tags ON Product.ProductID = Tags.ProductID where Product.ProductID = ?', product_id, function (error, results) {
        if (error) throw error;
        console.log(results)
        return res.send({ error: false, data: results, message: 'Product retrieved' });
    });
});

/* =========================================== */

/* Bind server เข้ากับ Port ที่กำหนด */
app.listen(process.env.PORT, () => {
    console.log(`Server listening on port: ${process.env.PORT}`);
});
