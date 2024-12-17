/* Import modules แต่ละส่วน  */
const express = require('express');
const dotenv = require('dotenv');
const path = require('path');
const app = express();
const cors = require('cors')
dotenv.config()
const port = process.env.PORT;

/* สร้าง Router object และ register the router */
const router = express.Router();
app.use(router);

router.use(express.json());
router.use(cors());
router.use(express.urlencoded({ extended: true }));
app.use("/", router);
app.use(express.static('public'))

/* ==================== Routing ======================= */

router.get("/Product", function (req, res) {
    console.log(`Request at ${req.url}`);
    res.sendFile(path.join(`${__dirname}/html/Product_Detail.html`));
});

router.get("/ProductManagement", async function (req, res) {
    console.log(`Request at ${req.url}`);
    res.sendFile(path.join(__dirname, 'html', 'Product_Manage.html'));    
});

router.get("/ProductEditAdd", async function (req, res) {
    console.log(`Request at ${req.url}`);
    res.sendFile(path.join(__dirname, 'html', 'Product_EDITADD.html'));
});

//app listen
app.listen(port, () => {
    console.log(`Server listening on port: ${port}`)
})
