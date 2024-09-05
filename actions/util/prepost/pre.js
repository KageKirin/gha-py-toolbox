const run = require("./run.js");

run(`${process.env.INPUT_SHELL} <<EOF
${process.env.INPUT_PRE}EOF`);
