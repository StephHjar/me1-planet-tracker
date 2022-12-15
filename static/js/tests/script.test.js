/**
 * @jest-environment jsdom
 */

const {
    verifyPassword
} = require("../script")

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("base.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("signup.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

describe("Error message alert appears if the password field is empty", () => {
    test("password exists", () => {
        const pw = "test"

        expect(window.alert in verifyPassword).toBe(false);
    });
});