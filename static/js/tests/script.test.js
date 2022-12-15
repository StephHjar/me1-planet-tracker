/**
 * @jest-environment jsdom
 */

// I received some help from ChatGPT to write these tests - credit in README

// Import the verifyPassword function to be tested
const {
    verifyPassword
} = require('../script');

// Create a mock for document.getElementById
const mockGetElementById = jest.spyOn(document, 'getElementById');

beforeAll(() => {
    // Create a mock for window.alert
    const mockAlert = jest.fn();
    // Tell the mock to do nothing when it is called
    mockAlert.mockImplementation(() => {});
    // Override the global window.alert function with the mock
    global.window.alert = mockAlert;
});

afterAll(() => {
    // Restore the original document.getElementById and window.alert functions
    mockGetElementById.mockRestore();
    global.window.alert = alert;
});

describe("verifyPassword function returns the correct alerts", () => {
    test("verifyPassword should return an alert if the password field is blank", () => {
        mockGetElementById.mockReturnValue({
            value: ''
        });
        expect(verifyPassword()).toBe(false);
    });
    test("verifyPassword should return an alert if the password is less than 8 characters", () => {
        mockGetElementById.mockReturnValue({
            value: "short"
        });
        expect(verifyPassword()).toBe(false);
    });
    test("verifyPassword should return an alert if the password is more than 15 characters", () => {
        mockGetElementById.mockReturnValue({
            value: "passwordistoolong"
        });
        expect(verifyPassword()).toBe(false);
    });
    test('verifyPassword should return no alert if the password is between 8 and 15 characters', () => {
        mockGetElementById.mockReturnValue({
            value: "test-password"
        });
        expect(verifyPassword()).toBe(true);
    });
});