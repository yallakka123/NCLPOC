@IsTest
private class PipelineTestTest {

    @IsTest
    static void testGetMessage() {
        System.assertEquals(
            'Pipeline Test Success',
            PipelineTest.getMessage()
        );
    }
}
