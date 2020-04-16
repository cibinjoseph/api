tree = Node('(object)', [
    Node('"cases_time_series" (array)', [
        Node('(object)', [
            Node('"dailyconfirmed" (string)'),
            Node('"dailydeceased" (string)'),
            Node('"dailyrecovered" (string)'),
            Node('"date" (string)'),
            Node('"totalconfirmed" (string)'),
            Node('"totaldeceased" (string)'),
            Node('"totalrecovered" (string)')
        ]),
    ]),
    Node('"statewise" (array)', [
        Node('(object)', [
            Node('"active" (string)'),
            Node('"confirmed" (string)'),
            Node('"deaths" (string)'),
            Node('"deltaconfirmed" (string)'),
            Node('"deltadeaths" (string)'),
            Node('"deltarecovered" (string)'),
            Node('"lastupdatedtime" (string)'),
            Node('"recovered" (string)'),
            Node('"state" (string)'),
            Node('"statecode" (string)'),
            Node('"statenotes" (string)')
        ])
    ]),
    Node('"tested" (array)', [
        Node('(object)', [
            Node('"positivecasesfromsamplesreported" (string)'),
            Node('"samplereportedtoday" (string)'),
            Node('"source" (string)'),
            Node('"testsconductedbyprivatelabs" (string)'),
            Node('"totalindividualstested" (string)'),
            Node('"totalpositivecases" (string)'),
            Node('"totalsamplestested" (string)'),
            Node('"updatetimestamp" (string)')
        ])
    ])
])
