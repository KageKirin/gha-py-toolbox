const run = require("./run.js");

run(`${process.env.INPUT_SHELL} -c "${escape(process.env.INPUT_POST)}"`);
