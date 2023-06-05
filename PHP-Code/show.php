<html>
    <head>
        <title>현재 상태</title>
    </head>
    <body>
        <header style="text-align:center;">
            <h1 style="display: inline-block; vertical-align: middle;">최근 건물 상태</h1>
            <button type="button" class="navyBtn" onClick="location.href='main.php'" style="float: left; display: inline-block; vertical-align: middle;">
            뒤로가기
            </button> <!-- 메인 화면 이동용 버튼 -->
        </header>
        <main>
            <?php
            error_reporting(E_ALL); # 에러체크용
            ini_set("display_errors", 1);

            header("Refresh:3"); # 3초마다 페이지가 새로고침됨 - 실시간 모니터링

            $connect = mysqli_connect("192.168.77.230","root","1234","embeded"); # MariaDB에 접속
            # MySQL의 데이터를 활용하기 위한 SQL문
            $sql1 = "SELECT gas FROM data ORDER BY id DESC LIMIT 1";
            $sql2 = "SELECT * FROM data";
            $sql3 = "SELECT flame FROM data ORDER BY id DESC LIMIT 1";
            $sql4 = "SELECT temp FROM data ORDER BY id DESC LIMIT 1";
            # 입력한 SQL문으로 MySQL과의 연동이 성공했는지를 저장
            $result1 = mysqli_query($connect, $sql1);
            $result2 = mysqli_query($connect, $sql2);
            $result3 = mysqli_query($connect, $sql3);
            $result4 = mysqli_query($connect, $sql4);
            # 화면출력에 활용햘 변수
            $gasinfo = " ";
            $flameinfo = " ";
            $tempinfo = " ";

            if(mysqli_num_rows($result1) > 0) { # 가스 누출 여부를 변수에 저장
                while($row = mysqli_fetch_array($result1)) {
                    if (intval($row["gas"]) >= 150) {
                        $gasinfo = "가스누출 심각!";
                        break;
                    }
                    else if (intval($row["gas"]) >= 80) {
                        $gasinfo = "가스누출 발생";
                        break;
                    }
                    else {
                        $gasinfo = "가스누출 없음";
                        break;
                    }
                }
            }

            if(mysqli_num_rows($result3) > 0) { # 화재 발생 여부를 변수에 저장
                while($row = mysqli_fetch_array($result3)) {
                    if (intval($row["flame"]) == 0) {
                        $flameinfo = "화재 발생!";
                        break;
                    }
                    else {
                        $flameinfo = "화재 미발생";
                        break;
                    }
                }
            }

            if(mysqli_num_rows($result4) > 0) { # 비정상적인 온도 상승 여부를 변수에 저장
                while($row = mysqli_fetch_array($result4)) {
                    if (intval($row["temp"]) >= 25) {
                        $tempinfo = "비정상 고온 감지";
                        break;
                    }
                    else {
                        $tempinfo = "정상 온도";
                        break;
                    }
                }
            }

            if(mysqli_num_rows($result2) > 0) # MySQL이 연결되었다면
            { # 표를 출력해 가장 최근 시점의 가스누출여부, 화재발생여부, 고온 여부를 출력함.
                $table1 = '
                <table border="1" align=middle style="display: inline-block; vertical-align: middle; text-align: center;">
                        <tr>
                            <th> 가스누출여부 </th>
                            <th> 화재발생여부 </th>
                            <th> 고온 여부 </th>
                        </tr>
                        <tr>
                            <td>'.$gasinfo.'</td>
                            <td>'.$flameinfo.'</td>
                            <td>'.$tempinfo.'</td>
                        </tr>
                </table>';
                echo $table1;
                # 디버깅용으로 MariaDB 내 테이블의 모든  출력
                $table2 = '
                <table border="1" align=right style="display: inline-block; vertical-align: middle;">
                        <tr>
                            <th> 타임스탬프 </th>
                            <th> 온도 </th>
                            <th> 가스농도 </th>
                            <th> 불꽃 </th>
                        </tr>
                ';
                while($row = mysqli_fetch_array($result2))
                {
                    $table2 .= '
                        <tr>
                            <td>'.$row["timestamp"].'</td>
                            <td>'.$row["temp"].'</td>
                            <td>'.$row["gas"].'</td>
                            <td>'.$row["flame"].'</td>
                        </tr>
                    ';
                }
                $table2 .= '</table>';
                echo $table2;
            }
        ?>
    </main>
    </body>
</html>
