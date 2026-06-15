import os
import sys
import pytest
from unittest.mock import MagicMock, patch

# Garante que o Python encontre a pasta raiz 'src' para os testes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.fraud_detector import FraudDetector

@pytest.fixture
def mock_neo4j_connection():
    """
    Fixture que intercepta a conexão real com o Neo4j e injeta um Mock.
    Impede que os testes unitários tentem acessar a internet ou gastem recursos do Aura.
    """
    with patch('src.services.fraud_detector.Neo4jConnection') as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance
        yield mock_instance

def test_detect_high_risk_patterns_with_fraud_present(mock_neo4j_connection):
    """
    Testa se o FraudDetector retorna e estrutura corretamente os dados
    quando a query do Neo4j encontra um padrão de triangulação de fraude.
    """
    # Cenário simulado de retorno do Neo4j (Massa de dados idêntica à real)
    mock_return_data = [{
        'dispositivo': 'IPHONE999',
        'ip_dispositivo': '192.168.1.10',
        'pix_destino': 'fraude@pix.com',
        'banco_destino': 'Banco X',
        'clientes': ['João Silva', 'Maria Souza', 'Pedro Santos'],
        'total_cpfs': 3
    }]
    
    # Configura o comportamento do mock para devolver a nossa massa simulada
    mock_neo4j_connection.query.return_value = mock_return_data
    
    # Execução do método sob teste
    detector = FraudDetector()
    resultados = detector.detect_high_risk_patterns()
    
    # Validações (Asserts) - Garantindo as premissas de negócio do Meigarom
    assert len(resultados) == 1, "Deveria ter encontrado exatamente 1 vetor de fraude."
    assert resultados[0]['dispositivo'] == 'IPHONE999', "O hardware identificado deveria ser o IPHONE999."
    assert resultados[0]['total_cpfs'] >= 3, "O gatilho de risco deveria apontar 3 ou mais CPFs conectados."
    assert 'Maria Souza' in resultados[0]['clientes'], "O nome dos clientes fraudadores deve estar mapeado na lista."
    
    # Confirma se a query foi disparada de fato no banco de dados
    mock_neo4j_connection.query.assert_called_once()

def test_detect_high_risk_patterns_empty_database(mock_neo4j_connection):
    """
    Testa o comportamento do sistema antifraude quando o banco de dados está limpo
    ou não existem padrões anômalos que atinjam a regra de negócio.
    """
    # Configura o banco para retornar uma lista vazia (nenhuma fraude detectada)
    mock_neo4j_connection.query.return_value = []
    
    detector = FraudDetector()
    resultados = detector.detect_high_risk_patterns()
    
    # Validações
    assert isinstance(resultados, list), "O retorno deve ser sempre uma lista do Python."
    assert len(resultados) == 0, "A lista de fraudes deve vir vazia se não houver anomalias na rede."
    mock_neo4j_connection.query.assert_called_once()
