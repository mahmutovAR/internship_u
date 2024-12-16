Feature: Drag and Drop testing

    Scenario: Drag and Drop
        Given DragAndDrop page
        When Drag and drop element into specified area
        Then After "Drag and Drop" action text in specified area changed