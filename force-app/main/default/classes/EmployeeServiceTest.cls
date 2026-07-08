@IsTest
private class EmployeeServiceTest {

    @IsTest
    static void testGetEmployeeName() {

        String result = EmployeeService.getEmployeeName();

        System.assertEquals(
            'John Doe',
            result
        );
    }
}
