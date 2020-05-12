Sub MultipleYearStockData()
    For Each ws In Worksheets
    ws.Activate
        ' Declare all variables
        Dim Columns_Vertical As Integer
        Dim OpeningYearDate As Boolean
        Dim OpeningYearPrice as Double
        Dim EndingYearPrice as Double
        Dim Ticker As String
        Dim TotalStockVolume As Double
        Dim Last_row_x As Long
        Dim YearlyChange as Double
        Dim PercentChange As Double
        Dim LocationTickerSymbol As Integer   
        Dim IncreaseMax as Long
        Dim DecreaseMax As Long
        Dim MaxVolume As Double

        Cells(1, 10).Value = "Ticker"
        Cells(1, 11).Value = "Yearly Change"
        Cells(1, 12).Value = "Percent Change"
        Cells(1, 13).Value = "Total Stock Volume"
        Cells(1, 16).Value = "Ticker"
        Cells(1, 17).Value = "Value"

        Cells(1, 15).Value = "Greatest % Increase"
        Cells(2, 15).Value = "Greatest % Decrease"
        Cells(3, 15).Value = "Greatest Total Volume"

        OpeningYearDate = True
        TotalStockVolume = 0
        LocationTickerSymbol = 2 

        ' Calculating the # of rows in each sheet of the excel file
        Last_row_x = ws.Cells(Rows.Count, 1).End(xlUp).Row

        For i = 2 To Last_row_x
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                
                Ticker = Cells(i, 1).Value
                TotalStockVolume = TotalStockVolume + Cells(i, 7).Value
                
                Range("J" & LocationTickerSymbol).Value = Ticker
                Range("M" & LocationTickerSymbol).Value = TotalStockVolume
                
                EndingYearPrice = Cells(i, 6).Value
                YearlyChange = EndingYearPrice - OpeningYearPrice
                Range("K" & LocationTickerSymbol).Value = YearlyChange
                        
                PercentChange = ((YearlyChange) / (OpeningYearPrice)) * 100
                Range("L" & LocationTickerSymbol).Value = PercentChange
                
                If Range("K" & LocationTickerSymbol).Value > 0 Then
                    Range("K" & LocationTickerSymbol).Interior.ColorIndex = 4
                Else
                    Range("K" & LocationTickerSymbol).Interior.ColorIndex = 3
                End If
                
                LocationTickerSymbol = LocationTickerSymbol + 1
                TotalStockVolume = 0
                OpeningYearDate = True
     
            Else
                TotalStockVolume = TotalStockVolume + Cells(i, 7).Value
                
                If OpeningYearDate And Cells(i, 3).Value <> 0 Then
                    OpeningYearPrice = Cells(i, 3).Value
                    OpeningYearDate = False
                End If       
            End If
        Next i
        IncreaseMax = 0
        DecreaseMax = 0
        MaxVolume = 0
        Columns_Vertical = ws.Cells(Rows.Count, 11).End(xlUp).Row
        For j = 2 To Columns_Vertical
            If Range("L" & j).Value > IncreaseMax Then
                IncreaseMax = Range("L" & j).Value
                Range("Q2").Value = IncreaseMax
                Range("P2").Value = Range("J" & j).Value          
            ElseIf Range("L" & j).Value < DecreaseMax Then
                DecreaseMax = Range("L" & j).Value
                Range("Q3").Value = Range("L" & j).Value
                Range("P3").Value = Range("J" & j).Value
            End If
            If Range("M" & j).Value > MaxVolume Then
                Max_Vol = Range("M" & j).Value
                Range("Q4").Value = MaxVolume
                Range("P4").Value = Range("J" & j).Value
            End If
        Next j
    Next ws
End Sub