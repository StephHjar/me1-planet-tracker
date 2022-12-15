/**
 * @jest-environment jsdom
 */

// Import the verifyPassword function that you want to test
const {
    verifyPassword
} = require('../script');

test('verifyPassword should return a window alert if the password field is blank', () => {
    // Create a mock for document.getElementById
    const mockGetElementById = jest.spyOn(document, 'getElementById');
    // Tell the mock to return a fake password input element when it is called
    mockGetElementById.mockReturnValue({
        value: ''
    });

    // Create a mock for window.alert
    const mockAlert = jest.fn();
    // Tell the mock to do nothing when it is called
    mockAlert.mockImplementation(() => {});
    // Override the global window.alert function with the mock
    global.window.alert = mockAlert;

    // Call the verifyPassword function and assert that it returns true
    expect(verifyPassword()).toBe(false);

    // Restore the original document.getElementById and window.alert functions
    mockGetElementById.mockRestore();
    global.window.alert = alert;
});

test('verifyPassword should return no window alert if the password is between 8 and 15 characters', () => {
    // Create a mock for document.getElementById
    const mockGetElementById = jest.spyOn(document, 'getElementById');
    // Tell the mock to return a fake password input element when it is called
    mockGetElementById.mockReturnValue({
        value: 'test-password'
    });

    // Create a mock for window.alert
    const mockAlert = jest.fn();
    // Tell the mock to do nothing when it is called
    mockAlert.mockImplementation(() => {});
    // Override the global window.alert function with the mock
    global.window.alert = mockAlert;

    // Call the verifyPassword function and assert that it returns true
    expect(verifyPassword()).toBe(true);

    // Restore the original document.getElementById and window.alert functions
    mockGetElementById.mockRestore();
    global.window.alert = alert;
});